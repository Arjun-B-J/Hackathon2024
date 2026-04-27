# Hackathon2024

A small Flask web service that accepts PDF file uploads and stores them in
Azure Blob Storage. Built as a hackathon prototype.

## Tech stack

- Python / Flask
- Azure Blob Storage (`azure-storage-blob`)

## Endpoints

- `GET /` — health/welcome message
- `GET /See Data` — returns the in-memory `data` list
- `POST /upload` — uploads a `.pdf` file (form field `file`) to the
  configured Azure container

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Fill in the Azure credentials at the top of `app.py`:
   - `STORAGE_ACCOUNT_KEY`
   - `STORAGE_ACCOUNT_NAME`
   - `CONNECTION_STRING`
   - `CONTAINER_NAME`

## Run

```
python -m flask run
```

## Files

- `app.py` — Flask application and routes
- `requirements.txt` — Python dependencies
