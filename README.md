# Address Book API

A REST API for managing an address book — create, update, delete addresses and find ones near a location.

Built with FastAPI, Pydantic v2, and SQLite.

---

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Swagger UI: http://127.0.0.1:8000/docs

---

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/address/` | Create an address |
| GET | `/address/{id}` | Get address by ID |
| PUT | `/address/{id}` | Update an address |
| DELETE | `/address/{id}` | Delete an address |
| GET | `/address/nearby` | Find addresses within a distance |

### Nearby search

```
GET /address/nearby?latitude=52.52&longitude=13.40&distance_km=10
```

Returns all addresses within the given radius using the Haversine formula.

---

## Project structure

```
app/
├── main.py        # App entry point, exception handlers
├── router.py      # Route definitions
├── service.py     # Business logic, distance calculation
├── repository.py  # SQL queries
├── schemas.py     # Pydantic request/response models
├── database.py    # SQLite connection
└── exceptions.py  # Domain exceptions
```
