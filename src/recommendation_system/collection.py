from chromadb import PersistentClient, Collection
from chromadb.api import ClientAPI
from chromadb.config import (
    DEFAULT_TENANT,
    DEFAULT_DATABASE,
    Settings
)

from src.config import settings


def _get_vector_store_client() -> ClientAPI:
    return PersistentClient(
        path=settings.vector_store.path,
        settings=Settings(),
        tenant=DEFAULT_TENANT,
        database=DEFAULT_DATABASE
    )


def get_collection(name: str) -> Collection:
    client = _get_vector_store_client()
    collection = client.get_collection(name)
    return collection
