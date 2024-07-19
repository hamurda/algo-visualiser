from fastapi import FastAPI

from .routers.arrays import array_routes

app = FastAPI()

app.include_router(array_routes.router)