from typing import Literal

from pydantic import BaseModel


class ExamSchema(BaseModel):
    name: Literal[
        "russian", 
        "social_science", 
        "math", 
        "physics", 
        "chemistry",
        "history",
        "informatics"
    ]
    points: int
