class InvalidInputError(Exception):
    def __init__(self, message="Invalid input provided."):
        self.message = message
        super().__init__(self.message)
        
class ItemNotFoundError(Exception):
    def __init__(self, item_id: int):
        self.message = f"Item with id {item_id} not found."
        super().__init__(self.message)



class SentinmentPiplineError(Exception):
    def __init__(self, message="Sentiment analysis pipeline is not initialized."):
        self.message = message
        super().__init__(self.message)


class PredictionError(Exception):
    def __init__(self, message="Prediction failed."):
        self.message = message
        super().__init__(self.message)