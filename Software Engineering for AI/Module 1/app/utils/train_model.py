from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os
from app.utils.logger import get_logger

logger = get_logger(__name__)

def train_and_save_model():
    try:
        iris = load_iris()
        logger.info("Loaded Iris dataset")

        X_train, X_test, y_train, y_test = train_test_split(
            iris.data, iris.target, test_size=0.2, random_state=42
        )
        logger.info("Split dataset into train/test")

        clf = RandomForestClassifier()
        clf.fit(X_train, y_train)
        logger.info("Model training complete")

        os.makedirs("app/models", exist_ok=True)
        joblib.dump(clf, "app/models/model.pkl")
        logger.info("Model saved to app/models/model.pkl")

    except Exception as e:
        logger.exception("Error during training or saving model.")
        raise
