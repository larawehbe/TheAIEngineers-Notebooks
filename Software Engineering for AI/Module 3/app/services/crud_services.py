from sqlalchemy.orm import Session
from app.models.item_model import Item
from app.schemas.items_schema import ItemCreate

def create_item(db: Session, item: ItemCreate):
    db_item = Item(name=item.name, value=item.value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def get_all_items(db: Session):
    return db.query(Item).all()

def update_item(db: Session, item_id: int, updated: ItemCreate):
    db_item = get_item(db, item_id)
    if db_item:
        db_item.name = updated.name
        db_item.value = updated.value
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
