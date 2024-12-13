from fastapi import FastAPI, responses

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/jobs")
def read_jobs():
    return responses.JSONResponse(content=[
        {
            "id": "3a2b1c",
            "title": "Tarefa de número 1",
            "periodicity": "1 * * * *",
            "status": True,
        },
        {
            "id": "4d5e6f",
            "title": "Tarefa de número 2",
            "periodicity": "2 * * * *",
            "status": False,
        },
        {
            "id": "7g8h9i",
            "title": "Tarefa de número 3",
            "periodicity": "3 * * * *",
            "status": True,
        },
    ])
