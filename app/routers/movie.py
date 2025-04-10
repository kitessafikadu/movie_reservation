from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, models, schemas, database

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.post("/", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(database.get_db)):
    return crud.create_movie(db=db, movie=movie)

@router.get("/", response_model=list[schemas.Movie])
def list_movies(db: Session = Depends(database.get_db)):
    return crud.get_movies(db)
