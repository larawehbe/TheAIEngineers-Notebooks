from pydantic import BaseModel

class TrainRequest(BaseModel):
    pass  # No input needed now

class PredictRequest(BaseModel):
    features: list[float]



class ItemBase(BaseModel):
    name: str
    value: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
