from typing import List

from src.recommendation_system.pipeline import create_pipeline
from src.recommendation_system.collection import get_collection
from src.schemas import VectorSchema, DirectionSchema


class DirectionsRecommendationSystem:
    _pipeline = create_pipeline()
    _collection = get_collection("applicants")

    def recommend(self, vector: VectorSchema) -> List[DirectionSchema]:
        dataframe = vector.to_dataframe()
        embedding = self._pipeline.transform(dataframe)
        recommendations = self._collection.query(query_embeddings=embedding)
