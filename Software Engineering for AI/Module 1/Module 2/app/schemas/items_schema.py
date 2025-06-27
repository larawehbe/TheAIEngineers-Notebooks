from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    value: float

class TrainRequest(BaseModel):
    pass  # No input needed now

class PredictRequest(BaseModel):
    features: list[float]
