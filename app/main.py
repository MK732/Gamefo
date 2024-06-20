from fastapi import FastAPI
from app.routers import games, genres, publishers, developers, platforms, release_dates
from dotenv import load_dotenv

load_dotenv(dotenv_path="/code/app/.env")

# Create a FastAPI instance
app = FastAPI(swagger_ui_parameters={"displayRequestDuration": True, "syntaxHighlight.activated" : False },
              
              title="GameFo API",
              description="An API to get information about games, genres, publishers, developers, and platforms.",
              openapi_url="/api/v2/openapi.json",
              
              )


# Include the routers
app.include_router(games.router)
app.include_router(genres.router)
app.include_router(publishers.router)
app.include_router(developers.router)
app.include_router(platforms.router)
app.include_router(release_dates.router)

# Root route
@app.get("/")
def all_routes():
    return {"Alas!": "You are home!"}


