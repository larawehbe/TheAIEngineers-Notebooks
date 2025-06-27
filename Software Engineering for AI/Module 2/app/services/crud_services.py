from app.schemas.items_schema import Item

db: dict[int, Item] = {}  # In-memory store

def create_item(item: Item):
    db[item.id] = item
    return item

def get_item(item_id: int):
    return db.get(item_id)

def update_item(item_id: int, item: Item):
    db[item_id] = item
    return item

def delete_item(item_id: int):
    return db.pop(item_id, None)

def list_items():
    return list(db.values())
