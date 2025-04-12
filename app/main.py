from fastapi import FastAPI
from app.routers import movie, reservation, user, auth,admin
from app.database import Base, engine
from app import models

app = FastAPI()

app.include_router(movie.router)
app.include_router(reservation.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(admin.router)

# Create all tables
Base.metadata.create_all(bind=engine)
