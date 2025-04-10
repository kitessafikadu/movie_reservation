from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, models, schemas, database

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db, user)

@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    return crud.get_user_by_id(db, user_id)
