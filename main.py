# main.py
from fastapi import FastAPI
from app.database.config import engine
from app.api.models.tablas import Base
from starlette.responses import RedirectResponse
from app.api.routers.endPoints import rutas

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)