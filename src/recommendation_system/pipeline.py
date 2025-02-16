from sklearn.pipeline import Pipeline

from src.recommendation_system.estimators import (
    SimpleImputer,
    GenderBinarizer,
    MilitaryServiceBinarizer,
    StandardScaler
)


def create_pipeline() -> Pipeline:
    return Pipeline([
        ("simple_imputer", SimpleImputer()),
        ("gender_binarizer", GenderBinarizer()),
        ("military_service_binarizer", MilitaryServiceBinarizer()),
        ("standard_scaler", StandardScaler())
    ])
