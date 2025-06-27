class ModelNotFoundException(Exception):
    """Raised when the model file is not found."""
    pass

class InvalidInputException(Exception):
    """Raised when input to the model is invalid."""
    pass
class TrainingError(Exception):
    """Raised when there is an error during model training."""
    pass