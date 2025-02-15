from typing import List, Literal, Dict

from pydantic import BaseModel

from src.schemas.exam import ExamSchema


class ApplicantSchema(BaseModel):
    gender: Literal["male", "female"]
    foreign_citizenship: str
    military_service: Literal["yes", "no"]
    gpa: float
    points: int
    bonus_points: int
    exams: List[ExamSchema]
    
    @property
    def exams_dict(self) -> Dict[str, int]:
        return {exam.name: exam.points for exam in self.exams}
