from fastapi import APIRouter
from app.schemas.items_schema import PredictRequest
from app.services.ml_services import train_model, predict_model

router = APIRouter(prefix="/ml", tags=["ML"])

@router.post("/train")
def train():
    return {"message": train_model()}

@router.post("/predict")
def predict(req: PredictRequest):
    prediction = predict_model(req.features)
    return {"prediction": prediction}
