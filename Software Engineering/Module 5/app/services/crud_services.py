from app.schemas.item_schema import ItemSchema
from app.utils.exceptions import ItemNotFoundError
from app.models.item_model import Item
from sqlalchemy.orm import Session


"""
input: 1, name: "Item1", value: 10.0
db[1] = Item(id=1, name="Item1", value=10.0)
db[2] = Item(id=2, name="Item2", value=20.0)
{
"id": 1, item: Item(id=1, name="Item1", value=10.0),
"id" : 2, item: Item(id=2, name="Item2", value=20.0)
}
"""
db: dict[int, Item] = {}

def create_item(db: Session, item: ItemSchema):
    # db_item = ItemModel(**item.dict())
    db_item = Item(name=item.name, value=item.value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
def get_item(db: Session, item_id) -> ItemSchema:
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise ItemNotFoundError(f"Item with id {item_id} not found")
    return db_item
def update_item(db: Session, item_id: int, item: ItemSchema) -> ItemSchema:
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise ItemNotFoundError(f"Item with id {item_id} not found")
    
    # Update the fields
    db_item.name = item.name
    db_item.value = item.value
    
    db.commit()
    db.refresh(db_item)
    return db_item

# todo: Make it with db
def delete_item(db: Session, item_id: int) -> ItemSchema:
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise ItemNotFoundError(f"Item with id {item_id} not found")    
    db.delete(db_item)
    db.commit()
    return db_item

def list_items(db: Session) :
    all_items = db.query(Item).all()
    if not all_items:
        raise ItemNotFoundError("No items found")
    
   
    return all_items


