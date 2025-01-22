import os, datetime, importlib.util
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI

scheduler = AsyncIOScheduler()

def load_jobs():
    for filename in os.listdir(os.path.join(os.path.dirname(__file__), 'jobs')):
        if filename.endswith('.py') and filename != '__init__.py':
            name = filename[:-3]
            spec = importlib.util.spec_from_file_location(name, os.path.join(os.path.dirname(__file__), 'jobs', filename))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, 'main') and hasattr(module, 'interval'):
                scheduler.add_job(module.main, 'interval', seconds=module.interval, kwargs={'file': filename,})

async def app(scope, receive, send):
    """Trivial example of an ASGI application."""
    if scope["type"] == "http":
        await receive()
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    [b"content-type", b"text/plain"],
                ],
            }
        )
        await send(
            {
                "type": "http.response.body",
                "body": b"Hello, world!",
                "more_body": False,
            }
        )
    elif scope["type"] == "lifespan":
        while True:
            message = await receive()
            if message["type"] == "lifespan.startup":
                load_jobs()
                scheduler.start()
                await send({"type": "lifespan.startup.complete"})
            elif message["type"] == "lifespan.shutdown":
                scheduler.shutdown()
                await send({"type": "lifespan.shutdown.complete"})
                return

async def scheduler_middleware(scope, receive, send):
    if scope['type'] == 'lifespan':
        async with AsyncIOScheduler() as scheduler:
            await app(scope, receive, send)
    else:
        await app(scope, receive, send)

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    load_jobs()
    scheduler.start()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/jobs")
async def read_jobs():
    jobs = []
    for job in scheduler.get_jobs():
        jobs.append({
            'id': job.id,
            'name': job.kwargs.get('file').removesuffix('.py'),
            'next_run_time': job.next_run_time.strftime('%d/%m/%Y - %H:%M:%S') if job.next_run_time else None,
        })
    return jobs

@app.get("/jobs/{job_id}")
async def read_job(job_id: str):
    job = scheduler.get_job(job_id)
    if job:
        return {
            'id': job.id,
            'name': job.kwargs.get('file').removesuffix('.py'),
            'next_run_time': job.next_run_time.strftime('%d/%m/%Y - %H:%M:%S') if job.next_run_time else None,
        }
    return {}

@app.get("/jobs/{job_id}/pause")
async def pause_job(job_id: str):
    job = scheduler.get_job(job_id)
    if job:
        scheduler.pause_job(job_id)
        return {
            'id': job.id,
            'name': job.kwargs.get('file').removesuffix('.py'),
            'next_run_time': job.next_run_time.strftime('%d/%m/%Y - %H:%M:%S') if job.next_run_time else None,
        }
    return {}

@app.get("/jobs/{job_id}/run")
async def run_job(job_id: str):
    job = scheduler.get_job(job_id)
    if job:
        await job.func()
        return {
            'id': job.id,
            'name': job.kwargs.get('file').removesuffix('.py'),
            'next_run_time': job.next_run_time.strftime('%d/%m/%Y - %H:%M:%S') if job.next_run_time else None,
        }
    return {}

@app.get("/jobs/{job_id}/resume")
async def resume_job(job_id: str):
    job = scheduler.get_job(job_id)
    if job:
        scheduler.resume_job(job_id)
        return {
            'id': job.id,
            'name': job.kwargs.get('file').removesuffix('.py'),
            'next_run_time': job.next_run_time.strftime('%d/%m/%Y - %H:%M:%S') if job.next_run_time else None,
        }