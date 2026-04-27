from fastapi import FastAPI
from src.utils.logger import logger
from src.routers.preprocess_router import router

app = FastAPI()

app.include_router(router)

@app.get("/")
async def root():

    logger.info("Root endpoint accessed")

    return {"message": "API is running"}
