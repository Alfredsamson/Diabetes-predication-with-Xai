# Machine Learning Web App (Iris Classifier)

A minimal FastAPI web app that trains an Iris classifier on startup (scikit-learn) and serves a small frontend to make predictions.

## Features
- Trains an Iris classifier (RandomForest) on startup
- REST API: `POST /api/predict`
- Static frontend at `/` with a modern, responsive form

## Requirements
- Python 3.9+

## Setup
```bash
cd /workspace
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## Run
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
Open your browser to `http://localhost:8000`.

## API
- POST `/api/predict`
  - Request JSON:
    ```json
    {
      "sepal_length": 5.1,
      "sepal_width": 3.5,
      "petal_length": 1.4,
      "petal_width": 0.2
    }
    ```
  - Response JSON:
    ```json
    {
      "predicted_class": "setosa",
      "probabilities": {
        "setosa": 0.98,
        "versicolor": 0.01,
        "virginica": 0.01
      }
    }
    ```

## Dev Tips
- Model retrains automatically on server start using the built-in Iris dataset (no network needed).
- Static files live in `static/`. Backend code is in `app/`.
