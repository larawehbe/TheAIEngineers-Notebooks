from fastapi import APIRouter, HTTPException
from app.services.ml_services import train_model, predict
from app.utils.exceptions import InvalidInputError
from app.schemas.ml_schema import PredictRequestSchema, PredictionSchema
from app.utils.logger import get_logger


logger = get_logger(__name__)

router = APIRouter(prefix="/ml", tags=["ml"])

@router.post("/train")
def train_model_route():
    try:
        train_model()
    except Exception as e:
        logger.error(f"An error occurred while training the model: {e}")
        raise HTTPException(status_code=500, detail="Model training failed")
    except FileNotFoundError as e:
        logger.error(f"File not found error: {e}")
        raise HTTPException(status_code=404, detail="Model file not found")
    return {"message": "Model trained successfully"}    

@router.post("/predict", response_model=PredictionSchema)
def predict_route(request: PredictRequestSchema):
    try:
        prediction = predict([request.input_data]) # [[5.1, 3.5, 1.4, 0.2]]
        #todo:
        # Add input_data, prediction to database table called predictions
    except InvalidInputError as e:
        logger.error(f"Invalid input error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"An error occurred during prediction: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed")
    return {"prediction": prediction[0]}

