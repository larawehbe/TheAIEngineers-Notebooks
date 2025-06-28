from pydantic import BaseModel


class Prediction(BaseModel):
    text: str
    sentiment: str

class PredictionCreate(BaseModel):
    text: str

