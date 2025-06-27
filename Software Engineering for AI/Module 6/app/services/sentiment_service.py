import re
from transformers import pipeline, Pipeline
from app.utils.logger import get_logger
from fastapi import HTTPException

logger = get_logger(__name__)

try:
    sentiment_pipeline: Pipeline = pipeline("sentiment-analysis")
    logger.info("Sentiment analysis pipeline loaded successfully.")
except Exception as e:
    logger.exception("Failed to load sentiment analysis pipeline.")
    raise RuntimeError("Could not initialize NLP model") from e

def preprocess_text(text: str) -> str:
    text = re.sub(r"http\S+|www.\S+", "", text)
    text = re.sub(r"[^A-Za-z0-9\s]", "", text)
    return text.strip().lower()

def analyze_sentiment(text: str):
    try:
        if not text or len(text.strip()) < 3:
            raise ValueError("Input text is too short or empty.")

        cleaned = preprocess_text(text)
        result = sentiment_pipeline(cleaned)[0]  # may raise if empty or invalid
        logger.info(f"Sentiment result: {result}")
        return {
            "cleaned_text": cleaned,
            "label": result["label"],
            "score": float(result["score"])
        }

    except ValueError as ve:
        logger.warning(f"Validation error: {ve}")
        raise HTTPException(status_code=422, detail=str(ve))

    except Exception as e:
        logger.exception("Error during sentiment analysis.")
        raise HTTPException(status_code=500, detail="Sentiment analysis failed.")
