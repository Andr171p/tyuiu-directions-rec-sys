from chromadb import PersistentClient
from chromadb.api import ClientAPI
from chromadb.config import (
    DEFAULT_TENANT,
    DEFAULT_DATABASE,
    Settings
)

from src.config import settings


class ChromaClientFactory:
    def __init__(
            self,
            path: str = settings.vector_store.path,
            config: Settings = Settings(),
            tenant: str = DEFAULT_TENANT,
            database: str = DEFAULT_DATABASE
    ) -> None:
        self._path = path
        self._config = config
        self._tenant = tenant
        self._database = database

    def create_chroma_client(self) -> ClientAPI:
        return PersistentClient(
            path=self._path,
            settings=self._config,
            tenant=self._tenant,
            database=self._database
        )
