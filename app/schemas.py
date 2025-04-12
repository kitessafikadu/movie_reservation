from pydantic import BaseModel
from typing import Optional
from datetime import datetime

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
class Showtime(BaseModel):
    id: int
    movie_id: int
    time: datetime
    ticket_price: int  # Assuming ticket price is an integer field

    class Config:
        orm_mode = True 

class ReservationReport(BaseModel):
    showtime_id: int
    movie_title: str
    total_reservations: int
    revenue: float
