from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pandas import DataFrame

from joblib import load
from sklearn.base import BaseEstimator, TransformerMixin

from src.config import settings


class MilitaryServiceBinarizer(BaseEstimator, TransformerMixin):
    def __init__(self, column: str = "military_service") -> None:
        self.column = column
        self._binarizer = load(settings.estimators.military_service_binarizer_path)

    def transform(self, X: "DataFrame") -> "DataFrame":
        X[self.column] = self._binarizer.transform(X[self.column])
        return X
