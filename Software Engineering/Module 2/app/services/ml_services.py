import os 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from app.utils.exceptions import InvalidInputError
from app.utils.logger import get_logger
logging = get_logger(__name__)

MODEL_PATH="app/models/iris_model.pkl"


logging = get_logger(__name__)

def train_model():
    try:
        # Load the iris dataset
        iris = load_iris()
        X, y = iris.data, iris.target

        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create a Random Forest Classifier
        model = RandomForestClassifier(n_estimators=100, random_state=42)

        # Train the model
        model.fit(X_train, y_train)

        # Save the model to a file
        
        joblib.dump(model, MODEL_PATH)
        logging.info(f"Model saved to {MODEL_PATH}")
    except FileNotFoundError as error:
        print(f"File not found error: {error}")
    except Exception as e:
        print(f"An error occurred while training the model: {e}")

        
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