from fastapi import APIRouter, Depends
from app.schemas.predictions_schema import Prediction, PredictionCreate
from app.services.sentiment_service import predict_sentiment
from app.utils.logger import get_logger
from app.dependencies import get_db
from sqlalchemy.orm import Session
from app.models.predictions_model import Predictions as PredictionsModel  # Import the model if needed for database operations

logging = get_logger(__name__)
router = APIRouter(prefix="/sentiment", tags=["Sentiment Analysis"])


@router.post("/predict", response_model=Prediction)
def predict_route(
    request: PredictionCreate,  db: Session= Depends(get_db)  # Dependency to get the database session, if needed
):
    """
    Predict the sentiment of the input text.
    :param prediction: The input text to analyze.
    :return: A dictionary with the sentiment label and score.
    """


    logging.info(f"Received prediction request: {request.text}")
    result = predict_sentiment(request.text)
    db_prediction_item = PredictionsModel(text=request.text, prediction=result['label'])  # Create a new prediction record in the database
    
    db.add(db_prediction_item)
    db.commit()  # Commit the transaction to save the prediction in the database
    db.refresh(db_prediction_item)
    logging.info(f"Prediction result: {result}")

    return Prediction(text=request.text, sentiment=result['label'])


@router.get("/", response_model=list[Prediction])
def get_predictions(db: Session = Depends(get_db)):
    """
    Get all predictions from the database.
    :return: A list of predictions.
    """
    logging.info("Fetching all predictions from the database.")
    predictions = db.query(PredictionsModel).all()
    return [Prediction(text=pred.text, sentiment=pred.prediction) for pred in predictions]