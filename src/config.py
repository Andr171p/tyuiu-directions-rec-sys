from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent


class EstimatorsSettings(BaseSettings):
    gender_binarizer_path: Path = BASE_DIR / "estimators" / "gender_binarizer.joblib"
    military_service_binarizer_path: Path = BASE_DIR / "estimators" / "military_service_binarizer.joblib"
    standard_scaler: Path = BASE_DIR / "estimators" / "standard_scaler.joblib"


class VectorStoreSettings(BaseSettings):
    path: Path = BASE_DIR / "chroma"


class Settings(BaseSettings):
    estimators: EstimatorsSettings = EstimatorsSettings()
    vector_store: VectorStoreSettings = VectorStoreSettings()


settings = Settings()
