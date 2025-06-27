from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import crud_services
from app.dependencies import get_db
from app.schemas.items_schema import Item, ItemCreate

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/", response_model=Item)
def create(item: ItemCreate, db: Session = Depends(get_db)):
    return crud_services.create_item(db, item)

@router.get("/{item_id}", response_model=Item)
def read(item_id: int, db: Session = Depends(get_db)):
    db_item = crud_services.get_item(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.get("/", response_model=list[Item])
def list_all(db: Session = Depends(get_db)):
    return crud_services.get_all_items(db)

@router.put("/{item_id}", response_model=Item)
def update(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    return crud_services.update_item(db, item_id, item)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return {"deleted": crud_services.delete_item(db, item_id)}
