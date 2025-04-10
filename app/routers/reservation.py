from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, models, schemas, database

router = APIRouter(prefix="/reservations", tags=["Reservations"])

@router.post("/", response_model=schemas.Reservation)
def create_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(database.get_db)):
    return crud.create_reservation(db, reservation)

@router.get("/", response_model=list[schemas.Reservation])
def get_user_reservations(db: Session = Depends(database.get_db)):
    return crud.get_all_reservations(db)
