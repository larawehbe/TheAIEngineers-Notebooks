import joblib
import numpy as np
import os
from app.utils.logger import get_logger
from app.utils.exceptions import ModelNotFoundException, InvalidInputException

logger = get_logger(__name__)

MODEL_PATH = "app/models/model.pkl"

def load_model():
    try:
        if not os.path.exists(MODEL_PATH):
            logger.error("Model file not found.")
            raise ModelNotFoundException("Model file is missing.")
        model = joblib.load(MODEL_PATH)
        logger.info("Model loaded successfully.")
        return model
    except Exception as e:
        logger.exception("Unexpected error loading model.")
        raise

def predict(input_features):
    try:
        if not isinstance(input_features, (list, np.ndarray)) or len(input_features) != 4:
            raise InvalidInputException("Input must be a list or array with 4 numerical values.")

        input_array = np.array(input_features, dtype=float)
        logger.info(f"Received input: {input_array.tolist()}")

        model = load_model()
        prediction = model.predict([input_array])
        logger.info(f"Prediction result: {prediction[0]}")
        return prediction[0]

    except (InvalidInputException, ModelNotFoundException) as known_error:
        logger.error(str(known_error))
        raise
    except Exception as e:
        logger.exception("Unknown error during prediction.")
        raise
