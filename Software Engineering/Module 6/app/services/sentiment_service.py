import re
from transformers import pipeline
from app.utils.logger import get_logger
from app.utils.exceptions import SentinmentPiplineError, PredictionError

logging = get_logger(__name__)

try:
    sentiment_pipeline = pipeline("sentiment-analysis")
except Exception as e:
    logging.error(f"Failed to load sentiment analysis pipeline: {e}")
    sentiment_pipeline = None
    raise SentinmentPiplineError("Sentiment analysis pipeline could not be initialized. Please check your environment and model availability.")


"""
sentiment_pipeline = load_custom_model()
"""


def preprocess_input(text: str) -> str:
    """
    Preprocess the input text for sentiment analysis.
    This can include lowercasing, removing special characters, etc.
    """
    # Example preprocessing: lowercasing and stripping whitespace
    text = text.lower().strip()
    # remove special characters if needed
    text = re.sub(r'[^\w\s]', '', text)
    #remove more special characters
    text = re.sub(r'\s+', ' ', text)
    #remove https links
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    return text


def predict_sentiment(text:str) -> dict:
    """
    Predict the sentiment of the input text.
    :param text: The input text to analyze.
    :return: A dictionary with the sentiment label and score.
    """
    if not sentiment_pipeline:
        raise SentinmentPiplineError("Sentiment analysis pipeline is not initialized.")

    if not text or len(text.strip()) == 0:
        raise ValueError("Input text cannot be empty.")

    preprocessed_text = preprocess_input(text)
    logging.info(f"Preprocessed text for sentiment analysis: {preprocessed_text}")

    try:
        result = sentiment_pipeline(preprocessed_text)[0]
        logging.info(f"Sentiment analysis result: {result}")
        result['label'] = result['label'].lower()  # Ensure label is in uppercase
        return result
    except Exception as e:
        logging.error(f"Error during sentiment analysis: {e}")
        raise PredictionError("Sentiment analysis failed.") from e

