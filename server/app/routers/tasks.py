from main import AVAILABLE_TASKS
from fastapi import APIRouter # type: ignore
from services import tasks

router = APIRouter(prefix="/tasks")

@router.get("/")
async def get_all_tasks():
    return tasks.get_all()

@router.post("/")
async def create_task(data: dict):
    return {"inserted_id": str(tasks.create(data).inserted_id)}