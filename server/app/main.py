import os
import fastapi  # type: ignore
import importlib  # type: ignore

# Inicializar FastAPI
app = fastapi.FastAPI()

# Caminho para arquivos de tarefas
TASKSPATH = os.path.join(os.path.dirname(__file__), "taskfile")
AVAILABLE_TASKS = os.listdir(TASKSPATH)

# Router para API principal
router = fastapi.APIRouter(prefix="/api/v1")

# Diretório de routers
ROUTERS_DIR = os.path.join(os.path.dirname(__file__), "routers")

# Iterar sobre os arquivos do diretório de routers
for filename in os.listdir(ROUTERS_DIR):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = f"routers.{filename[:-3]}"
        spec = importlib.util.spec_from_file_location(module_name, os.path.join(ROUTERS_DIR, filename))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Garantir que o módulo tem um router
        if hasattr(module, "router"):
            router.include_router(module.router)

# Incluir o router principal no app
app.include_router(router)

# Executar o servidor com Uvicorn
if __name__ == "__main__":
    import uvicorn  # type: ignore

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
