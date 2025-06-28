from app.schemas.item_schema import Item
from app.utils.exceptions import ItemNotFoundError
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

def create_item(item: Item) :
    db[item.id] = item
    return item

def get_item(item_id: int) -> Item:
    if item_id not in db:
        raise ItemNotFoundError(f"Item with id {item_id} not found")
    return db[item_id]

def update_item(item_id: int, item: Item) -> Item:
    if item_id not in db:
        raise ItemNotFoundError(f"Item with id {item_id} not found")
    db[item_id] = item
    return item

def delete_item(item_id: int) -> Item:
    if item_id not in db:
        raise ItemNotFoundError(f"Item with id {item_id} not found")
    return db.pop(item_id)

def list_items() -> list[Item]:
    return list(db.values())