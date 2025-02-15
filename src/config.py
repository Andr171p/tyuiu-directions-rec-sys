from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent


class VectorStoreSettings(BaseSettings):
    path: Path = BASE_DIR / "chroma"


class Settings(BaseSettings):
    vector_store: VectorStoreSettings = VectorStoreSettings()


settings = Settings()
