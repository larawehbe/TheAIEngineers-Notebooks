from fastapi import FastAPI
from app.routes import crud_routes, ml_routes
from app.utils.logger import get_logger
from app.database import Base, engine

logger = get_logger(__name__)
app = FastAPI(title="Clean ML API")

app.include_router(crud_routes.router)
app.include_router(ml_routes.router)

# Create DB tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"status": "ok"}
