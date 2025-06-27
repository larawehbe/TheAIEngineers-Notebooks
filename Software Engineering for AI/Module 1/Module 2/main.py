from fastapi import FastAPI
from app.routes import crud_routes, ml_routes
from app.utils.logger import get_logger

logger = get_logger(__name__)
app = FastAPI(title="Clean ML API")

app.include_router(crud_routes.router)
app.include_router(ml_routes.router)

@app.get("/")
def root():
    logger.info("Health check called.")
    return {"status": "ok"}
