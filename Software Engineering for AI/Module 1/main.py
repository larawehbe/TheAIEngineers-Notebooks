from app.utils.train_model import train_and_save_model
from app.services.predictor import predict
from app.utils.logger import get_logger
from app.utils.exceptions import ModelNotFoundException, InvalidInputException

logger = get_logger(__name__)

if __name__ == "__main__":
    try:
        logger.info("🚀 Starting AI pipeline")
        train_and_save_model()

        sample_input = [5.1, 3.5, 1.4, 0.2]
        result = predict(sample_input)
        logger.info(f"✅ Final prediction: {result}")

    except (ModelNotFoundException, InvalidInputException) as known_err:
        logger.error(f"Handled error: {str(known_err)}")

    except Exception as e:
        logger.exception("Unhandled fatal error.")
