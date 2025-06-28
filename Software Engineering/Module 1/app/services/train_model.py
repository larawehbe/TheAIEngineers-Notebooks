from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os 
from app.utils.logger import get_logger

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
        model_path = os.path.join('app/models', 'iris_model.pkl')
        joblib.dump(model, model_path)
        logging.info(f"Model saved to {model_path}")
    except FileNotFoundError as error:
        print(f"File not found error: {error}")
    except Exception as e:
        print(f"An error occurred while training the model: {e}")