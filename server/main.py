import fastapi, os, shutil, time, logging # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore

API = fastapi.FastAPI()

logging.basicConfig(filename="logs.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",)

API.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Origem permitida
    allow_credentials=True,  # Permitir envio de cookies (se necessário)
    allow_methods=["*"],  # Permitir todos os métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

# Middleware para log global
@API.middleware("http")
async def log_requests(request: fastapi.Request, call_next):
    # Captura o tempo inicial
    start_time = time.time()
    
    # Dados da requisição
    client_ip = request.client.host
    method = request.method
    url = str(request.url)
    headers = dict(request.headers)
    query_params = dict(request.query_params)
    body = await request.body()  # Captura o body da requisição

    # Processa a requisição
    response = await call_next(request)
    
    # Tempo de resposta
    process_time = time.time() - start_time
    status_code = response.status_code

    # Dados do log
    log_data = {
        "client_ip": client_ip,
        "method": method,
        "url": url,
        "status_code": status_code,
        "process_time": f"{process_time:.4f}s",
        "headers": headers,
        "query_params": query_params,
        "body": body.decode("utf-8") if body else "No body"
    }

    # Escreve o log
    logging.info(log_data)

    return response

UPLOAD_DIR = "tasks"  # Pasta onde os arquivos serão salvos
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Cria o diretório se não existir

tasks = []

@API.get("/api/v1")
async def health():
    response = {
        "header": {
            "status": "success",
            "message": "API Health.",
        },
        "data": "Hello World"
    }
    return fastapi.responses.JSONResponse(content = response, status_code = 200)

@API.get("/api/v1/task")
async def get_tasks():
    response = {
        "header": {
            "status": "success",
            "message": "List of available tasks.",
        },
        "data": tasks
    }

    return fastapi.responses.JSONResponse(content = response, status_code = 200)

@API.post("/api/v1/task")
async def create_task(
    name: str = fastapi.Form(...),
    description: str = fastapi.Form(...),
    file: fastapi.UploadFile = fastapi.File(...)
):

    if not file.filename.endswith(".py"):
        response = {
        "header": {
            "status": "failed",
            "message": "The uploaded file must have the extension .py",
            },
            "data": None
            }
        return fastapi.responses.JSONResponse(content = response, status_code = 300)

    if file.filename in os.listdir(UPLOAD_DIR):
        response = {
        "header": {
            "status": "failed",
            "message": "There is already a task registered with this file name",
            },
        "data": None
            }
        return fastapi.responses.JSONResponse(content = response, status_code = 300)

    id = 1

    if len(tasks) > 0:
        id = tasks[-1]["id"] + 1

    tasks.append(
        {
            "id": id,
            "name": name,
            "description": description,
            "filename": file.filename
        }
    )
    response = {
        "header": {
            "status": "success",
            "message": "Tasks created.",
            },
        "data": tasks[-1]
            }

    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return fastapi.responses.JSONResponse(content = response, status_code = 200)

@API.get("/api/v1/task/{id}")
async def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            response = {
                "header": {
                    "status": "success",
                    "message": "Tasks details."
                },
                "data": task
            }

            return fastapi.responses.JSONResponse(content = response, status_code = 200)