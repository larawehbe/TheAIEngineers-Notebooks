from typing import Optional
from pydantic import BaseModel

class ItemSchema(BaseModel):
    
    name: str
    value: float