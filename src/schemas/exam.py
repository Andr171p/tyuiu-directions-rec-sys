from pydantic import BaseModel


class ExamSchema(BaseModel):
    name: str
    points: int
