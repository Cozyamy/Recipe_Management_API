from fastapi import FastAPI
from routes import router as recipe_management_router
import config

app = FastAPI()

database = config.load_database()

app.include_router(recipe_management_router, prefix="/api")