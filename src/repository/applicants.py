from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from numpy import ndarray

import uuid

from src.vector_store.chroma_client_factory import ChromaClientFactory


class ChromaRepository:
    def __init__(self, collection_name: str = "applicants") -> None:
        chroma_client_factory = ChromaClientFactory()
        chroma_client = chroma_client_factory.create_chroma_client()
        self._collection = chroma_client.get_or_create_collection(collection_name)

    def add_embeddings(self, embeddings: "ndarray", metadatas: Optional[dict] = None) -> None:
        self._collection.add(
            ids=[str(uuid.uuid4())],
            embeddings=[embeddings.tolist()],
            metadatas=metadatas
        )

    def similarity_search(self, embeddings: "ndarray") -> dict:
        similar = self._collection.query(query_embeddings=embeddings)
        return similar
