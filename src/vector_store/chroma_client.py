from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from chromadb import Collection
    from chromadb.api import ClientAPI

from chromadb import PersistentClient
from chromadb.config import (
    DEFAULT_TENANT,
    DEFAULT_DATABASE,
    Settings
)

from src.config import settings


chroma_client = PersistentClient(
    path=settings.vector_store.path,
    settings=Settings(),
    tenant=DEFAULT_TENANT,
    database=DEFAULT_DATABASE
)


def get_or_create_collection(
        name: str,
        client: "ClientAPI" = chroma_client
) -> "Collection":
    collection = client.get_or_create_collection(name)
    return collection
