from typing import List

from pydantic import BaseModel

from src.schemas.direction import DirectionSchema


class RecommendationsSchema(BaseModel):
    directions: List[DirectionSchema]
