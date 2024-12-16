from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.triggers.cron import CronTrigger
from pymongo import MongoClient
import logging
from contextlib import asynccontextmanager
from pydantic import BaseModel
from typing import List, Dict, Any

# Configuração do logger
logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

# Conexão com o MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['scheduler_db']

# Defina a função que será agendada
def my_job(*args, **kwargs):
    print(f"Tarefa executada com args: {args} e kwargs: {kwargs}")

# Crie uma instância do agendador
scheduler = BackgroundScheduler()

# Adicione o MongoDBJobStore ao agendador
scheduler.add_jobstore(MongoDBJobStore(database='scheduler_db', collection='jobs', client=client))

# Crie a aplicação FastAPI
app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código para inicialização
    scheduler.start()
    yield
    # Código para desligamento
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

class JobParams(BaseModel):
    cron: str
    args: List[Any] = []
    kwargs: Dict[str, Any] = {}

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/jobs")
async def get_jobs():
    jobs = scheduler.get_jobs()
    jobs_info = []
    for job in jobs:
        jobs_info.append({
            "id": job.id,
            "name": job.name,
            "next_run_time": job.next_run_time.isoformat() if job.next_run_time else None,
            "trigger": str(job.trigger)
        })
    return JSONResponse(content=jobs_info)

@app.post("/job")
async def add_job(job_params: JobParams):
    # Crie um documento no MongoDB para obter um ID
    job_document = db.jobs.insert_one({})
    job_id = str(job_document.inserted_id)
    
    # Adicione o job ao agendador usando o ID do MongoDB
    scheduler.add_job(my_job, CronTrigger.from_crontab(job_params.cron), id=job_id, args=job_params.args, kwargs=job_params.kwargs)
    return {"message": "Job added", "job_id": job_id}

@app.delete("/job/{job_id}")
async def remove_job(job_id: str):
    scheduler.remove_job(job_id)
    return {"message": "Job removed"}