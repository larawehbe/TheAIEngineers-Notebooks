from app.database import Base

from sqlalchemy import Column, Integer, String, Float

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(Float)

    
# class Item(BaseModel):
#     id: int
#     name: str
#     value: float

