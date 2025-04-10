from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# === User CRUD ===
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# === Movie CRUD ===
def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def get_movies(db: Session):
    return db.query(models.Movie).all()


# === Reservation CRUD ===
def create_reservation(db: Session, reservation: schemas.ReservationCreate):
    db_res = models.Reservation(**reservation.dict())
    db.add(db_res)
    db.commit()
    db.refresh(db_res)
    return db_res

def get_all_reservations(db: Session):
    return db.query(models.Reservation).all()


# === Authentication ===
def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user or not pwd_context.verify(password, user.hashed_password):
        return None
    return user
