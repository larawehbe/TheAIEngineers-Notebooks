from fastapi import APIRouter
from app.services.crud_services import (
    create_item,
    get_item,
    update_item,
    delete_item,
    list_items
)
from app.schemas.items_schema import Item
router = APIRouter(prefix="/items", tags=["CRUD"])

@router.post("/", response_model=Item)
def create(item: Item):
    return create_item(item)

@router.get("/{item_id}", response_model=Item)
def read(item_id: int):
    return get_item(item_id)

@router.put("/{item_id}", response_model=Item)
def update(item_id: int, item: Item):
    return update_item(item_id, item)

@router.delete("/{item_id}")
def delete(item_id: int):
    return {"deleted": delete_item(item_id)}

@router.get("/", response_model=list[Item])
def list_all():
    return list_items()
