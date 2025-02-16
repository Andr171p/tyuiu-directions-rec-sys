from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from numpy import ndarray
    from pandas import DataFrame

from joblib import load
from sklearn.base import BaseEstimator, TransformerMixin

from src.config import settings


class StandardScaler(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        self._scaler = load(settings.estimators.standard_scaler)

    def transform(self, X: "DataFrame") -> "ndarray":
        X_scaled = self._scaler.transform(X)
        return X_scaled
