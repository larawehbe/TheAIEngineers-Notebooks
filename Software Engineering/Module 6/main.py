from fastapi import FastAPI, HTTPException

from app.utils.exceptions import InvalidInputError
from app.utils.logger import get_logger
from app.routes.crud_routes import router as crud_router
from app.routes.ml_routes import router as ml_router
from app.routes.sentimnet_routes import router as sentiment_router
from app.database import Base, engine


logger = get_logger(__name__)
logger.info("Starting the model training process...")


app = FastAPI(title="Iris Flower Prediction API")
app.include_router(crud_router)
app.include_router(ml_router)
app.include_router(sentiment_router)
Base.metadata.create_all(bind=engine)  # Create database tables

@app.get("/")
def root():
    return {"status": "API is running"}


@app.get("/healtcheck")
def root():
    return {"status": "Healthcheck is running"}



@app.post("/name")
def name(name: str):
    if not name:
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    return {"message": f"Hello, {name}!"}