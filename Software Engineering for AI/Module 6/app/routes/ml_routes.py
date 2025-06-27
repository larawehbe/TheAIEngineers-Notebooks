from fastapi import APIRouter, HTTPException
from app.schemas.sentiment_schema import SentimentRequest, SentimentResponse
from app.services.sentiment_service import analyze_sentiment
from app.utils.logger import get_logger

router = APIRouter(prefix="/nlp", tags=["NLP"])
logger = get_logger(__name__)

@router.post("/sentiment", response_model=SentimentResponse)
def sentiment(request: SentimentRequest):
    try:
        logger.info(f"Incoming sentiment request: {request.text}")
        return analyze_sentiment(request.text)

    except HTTPException as e:
        # Re-raise FastAPI-aware exceptions
        logger.warning(f"Handled error in route: {e.detail}")
        raise e

    except Exception as e:
        logger.exception("Unexpected error in /nlp/sentiment route.")
        raise HTTPException(
            status_code=500,
            detail="Internal error occurred while analyzing sentiment."
        )
