from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from datetime import date
from app import crud, models, schemas, database

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.post("/", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(database.get_db)):
    return crud.create_movie(db=db, movie=movie)

@router.get("/", response_model=list[schemas.Movie])
def list_movies(db: Session = Depends(database.get_db)):
    return crud.get_movies(db)
@router.get("/showtimes", response_model=list[schemas.Showtime])
def get_showtimes_for_date(db: Session = Depends(database.get_db), show_date: date = None):
    if not show_date:
        raise HTTPException(status_code=400, detail="Date is required")

    showtimes = db.query(models.Showtime).filter(models.Showtime.time.like(f'{show_date}%')).all()
    
    if not showtimes:
        raise HTTPException(status_code=404, detail="No showtimes found for this date")

    return showtimes