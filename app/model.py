from __future__ import annotations

from typing import Dict, List
import math


class ModelService:
    def __init__(self) -> None:
        # Class centroids computed from the Iris dataset means
        # Order of features: sepal_length, sepal_width, petal_length, petal_width
        self.class_names = ["setosa", "versicolor", "virginica"]
        self.centroids: Dict[str, List[float]] = {
            "setosa": [5.006, 3.418, 1.464, 0.244],
            "versicolor": [5.936, 2.770, 4.260, 1.326],
            "virginica": [6.588, 2.974, 5.552, 2.026],
        }

    @staticmethod
    def _euclidean_distance(a: List[float], b: List[float]) -> float:
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

    def predict(self, features: List[float]) -> Dict[str, float]:
        # Compute distances to each class centroid
        distances: Dict[str, float] = {
            label: self._euclidean_distance(features, centroid)
            for label, centroid in self.centroids.items()
        }

        # Convert distances to probabilities via softmax over negative distances
        # p(class) = exp(-d) / sum(exp(-d_i))
        exps = {k: math.exp(-d) for k, d in distances.items()}
        total = sum(exps.values())
        probabilities = {k: (v / total if total > 0 else 0.0) for k, v in exps.items()}
        return probabilities