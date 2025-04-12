from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from datetime import date
from app import crud, models, schemas, database

router = APIRouter(prefix="/reservations", tags=["Reservations"])

@router.post("/", response_model=schemas.Reservation)
def create_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(database.get_db)):
    return crud.create_reservation(db, reservation)

@router.get("/", response_model=list[schemas.Reservation])
def get_user_reservations(db: Session = Depends(database.get_db)):
    return crud.get_all_reservations(db)
@router.delete("/reservations/{reservation_id}")
def cancel_reservation(reservation_id: int, db: Session = Depends(database.get_db)):
    reservation = db.query(models.Reservation).filter(models.Reservation.id == reservation_id).first()
    
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    
    showtime_time = reservation.showtime.time
    if showtime_time < datetime.now():
        raise HTTPException(status_code=400, detail="Cannot cancel past reservations")

    db.delete(reservation)
    db.commit()
    
    return {"message": "Reservation canceled successfully"}