from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .model import ModelService
from .schemas import PredictRequest, PredictResponse


BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(title="ML Web App - Iris Classifier")

# CORS can be relaxed if you plan to serve frontend separately
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static assets
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Initialize model service
model_service = ModelService()


@app.get("/")
async def root() -> FileResponse:
    index_file = STATIC_DIR / "index.html"
    return FileResponse(str(index_file))


@app.post("/api/predict", response_model=PredictResponse)
async def predict(payload: PredictRequest) -> PredictResponse:
    try:
        features: List[float] = [
            payload.sepal_length,
            payload.sepal_width,
            payload.petal_length,
            payload.petal_width,
        ]
        probabilities: Dict[str, float] = model_service.predict(features)
        predicted_class = max(probabilities, key=probabilities.get)
        return PredictResponse(predicted_class=predicted_class, probabilities=probabilities)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=400, detail=str(exc)) from exc