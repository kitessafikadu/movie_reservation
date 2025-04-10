# Movie Reservation System

A backend system for movie ticket reservations. Users can sign up, log in, browse movies, reserve seats for specific showtimes, and manage their reservations. Admin users can manage movies and view reservation reports.

---

## 🛠️ **Technologies Used**

- **FastAPI**: Web framework for building the API.
- **SQLite**: Database for storing movies, reservations, and users.
- **SQLAlchemy**: ORM for interacting with the SQLite database.
- **Pydantic**: Data validation and serialization.
- **JWT**: Token-based authentication for users and admins.
- **Bcrypt**: Password hashing for security.

---

## 🚀 **Installation**

### Prerequisites

Ensure you have **Python 3.8+** installed.

1. Clone the repository:

   ```bash
   git clone https://github.com/kitessafikadu/movie_reservation_system.git
   cd movie_reservation_system
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚡ **Running the Application**

1. Run the FastAPI app:

   ```bash
   uvicorn app.main:app --reload
   ```

   This will start the server at `http://127.0.0.1:8000`.

2. You can access the **Swagger UI** at `http://127.0.0.1:8000/docs` for API documentation.
