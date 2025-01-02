from fastapi import APIRouter # type: ignore

router = APIRouter(prefix="/queue")

@router.get("/")
async def health():
    return {"message": "queue"}