import os
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from app.utils.logger import get_logger
from app.utils.exceptions import InvalidInputException, ModelNotFoundException

logger = get_logger(__name__)
MODEL_PATH = "app/models/model.pkl"

def train_model():
    iris = load_iris()
    X, y = iris.data, iris.target
    clf = RandomForestClassifier()
    clf.fit(X, y)
    os.makedirs("app/models", exist_ok=True)
    joblib.dump(clf, MODEL_PATH)
    logger.info("Model trained and saved.")
    return "Training complete."

def predict_model(features: list[float]):
    if len(features) != 4:
        raise InvalidInputException("Expected 4 features.")
    if not os.path.exists(MODEL_PATH):
        raise ModelNotFoundException("Trained model not found.")
    model = joblib.load(MODEL_PATH)
    pred = model.predict([features])[0]
    return int(pred)
