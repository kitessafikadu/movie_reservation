from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas, database
from app.auth import get_current_admin

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db, user)

@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    return crud.get_user_by_id(db, user_id)

@router.post("/make-admin/{user_id}")
def promote_user_to_admin(user_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_admin)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_admin = True
    db.commit()
    return {"msg": f"{user.username} has been promoted to admin"}

