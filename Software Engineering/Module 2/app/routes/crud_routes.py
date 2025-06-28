# CRUD: Create, Read, Update, Delete
from fastapi import APIRouter, HTTPException
from app.schemas.item_schema import Item
from app.services.crud_services import create_item, get_item, update_item, delete_item, list_items
from app.utils.exceptions import ItemNotFoundError


router = APIRouter(prefix="/items", tags=["items"])

# POST locahost:8000/items
@router.post("/", response_model=Item)
def create_item_route(item: Item):
    """
    Create a new item.
    """
    return create_item(item)


@router.get("/{item_id}", response_model=Item)
def get_item_route(item_id: int):
    """
    Get an item by its ID.
    """
    try:
        return get_item(item_id)
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.put("/{item_id}", response_model=Item)
def update_item_route(item_id: int, item: Item):
    """
    Update an existing item by its ID.
    """
    try:
        return update_item(item_id, item)
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/{item_id}", response_model=Item)
def delete_item_route(item_id: int):
    """
    Delete an item by its ID.
    """
    try:
        return delete_item(item_id)
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/", response_model=list[Item])
def list_items_route():
    """
    List all items.
    """
    return list_items()