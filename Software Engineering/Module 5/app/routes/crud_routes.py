# CRUD: Create, Read, Update, Delete
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.item_schema import ItemSchema
from app.services.crud_services import create_item, get_item, update_item, delete_item, list_items
from app.utils.exceptions import ItemNotFoundError
from app.dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/items", tags=["items"])

# POST locahost:8000/items
@router.post("/", response_model=ItemSchema)
def create_item_route( item: ItemSchema, db: Session = Depends(get_db)):
    """
    Create a new item.
    """
    return create_item(db, item)


@router.get("/{item_id}", response_model=ItemSchema)
def get_item_route(item_id: int, db: Session = Depends(get_db)):
    """
    Get an item by its ID.
    """
    try:
        return get_item(db,item_id)
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.put("/{item_id}", response_model=ItemSchema)
def update_item_route(item_id: int, item: ItemSchema, db: Session = Depends(get_db)):
    """
    Update an existing item by its ID.
    """
    try:
        return update_item(db,item_id, item)
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/{item_id}", response_model=ItemSchema )
def delete_item_route(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item by its ID.
    """
    try:
        return delete_item(db,item_id)
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/", response_model=list[ItemSchema])
def list_items_route(db: Session = Depends(get_db)):
    """
    List all items.
    """
    all_items = list_items(db)
    all_items_schema = []
    for x in all_items:
        x_item = ItemSchema(id=x.id, name=x.name, value=x.value)
        all_items_schema.append(x_item)
    return all_items_schema