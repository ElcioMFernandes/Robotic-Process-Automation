from fastapi import FastAPI, HTTPException, responses
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurações de CORS para http://localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000/"],  # Apenas esta origem é permitida
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Dados simulados
jobs = [
    {
        "id": "64b2a1d4c6f8e1e76293f1a1",
        "title": "Tarefa 1",
        "description": "Descrição da tarefa de número 1",
        "periodicity": "1 * * * *",
        "args": [1, 10, 100],
        "kwargs": {
            "string": "1",
            "integer": 1,
            "float": 1.1,
            "bool": True,
        },
        "status": False,
    },
    {
        "id": "64b2a1d4c6f8e1e76293f1a2",
        "title": "Tarefa 2",
        "description": "Descrição da tarefa de número 2",
        "periodicity": "2 * * * *",
        "args": [2, 20, 200],
        "kwargs": {
            "string": "2",
            "integer": 2,
            "float": 2.2,
            "bool": True,
        },
        "status": False,
    },
    {
        "id": "64b2a1d4c6f8e1e76293f1a3",
        "title": "Tarefa 3",
        "description": "Descrição da tarefa de número 3",
        "periodicity": "3 * * * *",
        "args": [3, 30, 300],
        "kwargs": {
            "string": "3",
            "integer": 3,
            "float": 3.3,
            "bool": True,
        },
        "status": True,
    },
    {
        "id": "64b2a1d4c6f8e1e76293f1a4",
        "title": "Tarefa 4",
        "description": "Descrição da tarefa de número 4",
        "periodicity": "4 * * * *",
        "args": [4, 40, 400],
        "kwargs": {
            "string": "4",
            "integer": 4,
            "float": 4.4,
            "bool": False,
        },
        "status": False,
    },
    {
        "id": "64b2a1d4c6f8e1e76293f1a5",
        "title": "Tarefa 5",
        "description": "Descrição da tarefa de número 5",
        "periodicity": "5 * * * *",
        "args": [5, 50, 500],
        "kwargs": {
            "string": "5",
            "integer": 5,
            "float": 5.5,
            "bool": True,
        },
        "status": True,
    },
    {
        "id": "64b2a1d4c6f8e1e76293f1a6",
        "title": "Tarefa 6",
        "description": "Descrição da tarefa de número 6",
        "periodicity": "6 * * * *",
        "args": [6, 60, 600],
        "kwargs": {
            "string": "6",
            "integer": 6,
            "float": 6.6,
            "bool": False,
        },
        "status": False,
    },
    {
        "id": "64b2a1d4c6f8e1e76293f1a7",
        "title": "Tarefa 7",
        "description": "Descrição da tarefa de número 7",
        "periodicity": "7 * * * *",
        "args": [7, 70, 700],
        "kwargs": {
            "string": "7",
            "integer": 7,
            "float": 7.7,
            "bool": True,
        },
        "status": True,
    },
    {
        "id": "64b2a1d4c6f8e1e76293f1a8",
        "title": "Tarefa 8",
        "description": "Descrição da tarefa de número 8",
        "periodicity": "8 * * * *",
        "args": [8, 80, 800],
        "kwargs": {
            "string": "8",
            "integer": 8,
            "float": 8.8,
            "bool": False,
        },
        "status": False,
    },
    {
        "id": "64b2a1d4c6f8e1e76293f1a9",
        "title": "Tarefa 9",
        "description": "Descrição da tarefa de número 9",
        "periodicity": "9 * * * *",
        "args": [9, 90, 900],
        "kwargs": {
            "string": "9",
            "integer": 9,
            "float": 9.9,
            "bool": True,
        },
        "status": True,
    },
    {
        "id": "64b2a1d4c6f8e1e76293f1aa",
        "title": "Tarefa 10",
        "description": "Descrição da tarefa de número 10",
        "periodicity": "10 * * * *",
        "args": [10, 100, 1000],
        "kwargs": {
            "string": "10",
            "integer": 10,
            "float": 10.1,
            "bool": True,
        },
        "status": True,
    },
]


@app.get("/jobs")
async def read_jobs():
    return responses.JSONResponse(content=jobs)

@app.get("/job/{id}")
async def read_job(id: str):
    # Procura o job pelo ID
    job = next((job for job in jobs if job["id"] == id), None)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return responses.JSONResponse(content=job)
