from pydantic import BaseModel
from typing import Optional

# === Movie Schemas ===
class MovieBase(BaseModel):
    title: str
    description: str
    poster_url: str
    genre: str

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


# === Reservation Schemas ===
class ReservationCreate(BaseModel):
    user_id: int
    showtime_id: int
    seat_number: str

class Reservation(ReservationCreate):
    id: int

    class Config:
        orm_mode = True


# === User Schemas ===
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_admin: bool

    class Config:
        orm_mode = True
