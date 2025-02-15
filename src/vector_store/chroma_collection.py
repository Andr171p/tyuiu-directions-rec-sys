from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    import numpy as np
    from chromadb import Collection

import uuid

from src.vector_store.chroma_client import get_or_create_collection


class ChromaCollection:
    def __init__(
            self,
            collection: "Collection" = get_or_create_collection("applicants")
    ) -> None:
        self._collection = collection

    def add(self, embeddings: "np.ndarray", metadatas: Optional[dict] = None) -> None:
        self._collection.add(
            ids=[str(uuid.uuid4())],
            embeddings=[embeddings.tolist()],
            metadatas=metadatas,
        )

    def similarity_search(self, embeddings: "np.ndarray") -> dict:
        result = self._collection.query(query_embeddings=embeddings)
        return result
