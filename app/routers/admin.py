from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas, database

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/admin/reports/reservations", response_model=list[schemas.ReservationReport])
def get_reservation_report(db: Session = Depends(database.get_db)):
    showtimes = db.query(models.Showtime).all()
    report = []

    for showtime in showtimes:
        total_reservations = len(showtime.reservations)
        revenue = total_reservations * showtime.ticket_price
        report.append({
            "showtime_id": showtime.id,
            "movie_title": showtime.movie.title,
            "total_reservations": total_reservations,
            "revenue": revenue
        })

    return report
