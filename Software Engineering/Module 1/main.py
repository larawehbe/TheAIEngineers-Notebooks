from app.services.train_model import train_model
from app.services.predictor import predict
from app.utils.exceptions import InvalidInputError
from app.utils.logger import get_logger



logger = get_logger(__name__)
logger.info("Starting the model training process...")


train_model()

#sepal length, sepal width, petal length, petal width
try:
    data_input = [[5.1, 3.5, 1.4, 0.2]]  # Example input data
    logger.debug(f"Input data for prediction: {data_input}")
    prediction = predict(data_input)
    logger.info(f"Prediction: {prediction}")

except InvalidInputError as e:
    logger.error(f"Invalid input error: {e.message}")