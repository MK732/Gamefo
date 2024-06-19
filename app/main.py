from typing import Union
from fastapi import FastAPI
from app.routers import games, genres,publishers
from dotenv import load_dotenv

load_dotenv(dotenv_path="/code/app/.env")

# Create a FastAPI instance
app = FastAPI()


app.include_router(games.router)
app.include_router(genres.router)
app.include_router(publishers.router)
# Root route
@app.get("/")
def all_routes():
    return {"Alas!": "You are home!"}


