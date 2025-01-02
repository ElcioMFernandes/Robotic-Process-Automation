from fastapi import APIRouter # type: ignore

router = APIRouter(prefix="/triggers")

@router.get("/")
async def health():
    return {"message": "triggers"}