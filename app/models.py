from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.schema import UniqueConstraint
from app.database import Base
from datetime import datetime

# === User Model ===
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

    reservations = relationship("Reservation", back_populates="user")


# === Movie Model ===
class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    poster_url = Column(String)
    genre = Column(String)

    showtimes = relationship("Showtime", back_populates="movie")


# === Showtime Model ===
class Showtime(Base):
    __tablename__ = "showtimes"

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    time = Column(DateTime, nullable=False)

    movie = relationship("Movie", back_populates="showtimes")
    reservations = relationship("Reservation", back_populates="showtime")


# === Reservation Model ===
class Reservation(Base):
    __tablename__ = "reservations"
    __table_args__ = (UniqueConstraint('showtime_id', 'seat_number', name='unique_seat_reservation'),)

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    showtime_id = Column(Integer, ForeignKey("showtimes.id"))
    seat_number = Column(Integer)

    user = relationship("User", back_populates="reservations")
    showtime = relationship("Showtime", back_populates="reservations")

# class Showtime(Base):
#     __tablename__ = "showtimes"

#     id = Column(Integer, primary_key=True, index=True)
#     movie_id = Column(Integer, ForeignKey("movies.id"))
#     time = Column(DateTime)
#     ticket_price = Column(Integer)  # New field for ticket price

#     movie = relationship("Movie", back_populates="showtimes")
#     reservations = relationship("Reservation", back_populates="showtime")

