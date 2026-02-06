from pydantic import BaseModel, Field
from typing import Dict


class PredictRequest(BaseModel):
    sepal_length: float = Field(..., description="Sepal length in cm")
    sepal_width: float = Field(..., description="Sepal width in cm")
    petal_length: float = Field(..., description="Petal length in cm")
    petal_width: float = Field(..., description="Petal width in cm")


class PredictResponse(BaseModel):
    predicted_class: str
    probabilities: Dict[str, float]