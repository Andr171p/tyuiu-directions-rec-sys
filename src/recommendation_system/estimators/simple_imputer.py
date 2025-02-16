from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from pandas import DataFrame

from sklearn.base import BaseEstimator, TransformerMixin


class SimpleImputer(BaseEstimator, TransformerMixin):
    def __init__(self, columns: Optional[List[str]] = None) -> None:
        self.columns = columns

    def transform(self, X: "DataFrame") -> "DataFrame":
        if self.columns is not None:
            X[self.columns] = X[self.columns].fillna(0)
        X = X.fillna(0)
        return X
