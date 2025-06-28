import joblib
from app.utils.exceptions import InvalidInputError
from app.utils.logger import get_logger
logging = get_logger(__name__)

MODEL_PATH="app/models/iris_model.pkl"


def load_model():
    model = joblib.load(MODEL_PATH)
    return model


def predict(input_data):
    
    if len(input_data[0]) <4 or len(input_data[0]) != 4:
        logging.error("Input data must contain exactly 4 features: sepal length, sepal width, petal length, and petal width.")
        raise InvalidInputError("Input data must contain exactly 4 features: sepal length, sepal width, petal length, and petal width.")
    model = load_model()


    try:
        logging.debug(f"Input data for prediction: {input_data}")
        logging.info("Making prediction...")
        prediction = model.predict(input_data)
    except Exception as error:
        logging.error(f"An error occurred during prediction: {error}")
        return None
    return prediction