from server.core.decorators import task
import asyncio

@task("example")
async def main(*args, **kwargs):
    print("Example task.")

interval = 5