from typing import Literal, Optional

from numpy import ndarray
from pandas import DataFrame
from pydantic import BaseModel

from src.schemas.applicant import ApplicantSchema


class VectorSchema(BaseModel):
    gender: Literal["male", "female"]
    foreign_citizenship: str
    military_service: Literal["yes", "no"]
    gpa: float
    points: int
    bonus_points: int
    russian: Optional[int]
    social_science: Optional[int]
    math: Optional[int]
    physics: Optional[int]
    chemistry: Optional[int]
    history: Optional[int]
    informatics: Optional[int]
    
    @classmethod
    def from_applicant(cls, applicant: ApplicantSchema) -> "VectorSchema":
        return cls(
            gender=applicant.gender,
            foreign_citizenship=applicant.foreign_citizenship,
            military_service=applicant.military_service,
            gpa=applicant.gpa,
            points=applicant.points,
            bonus_points=applicant.bonus_points,
            russian=applicant.exams_dict.get("russian"),
            social_science=applicant.exams_dict.get("social_science"),
            math=applicant.exams_dict.get("math"),
            physics=applicant.exams_dict.get("physics"),
            chemistry=applicant.exams_dict.get("chemistry"),
            history=applicant.exams_dict.get("history"),
            informatics=applicant.exams_dict.get("informatics")
        )
        
    def to_dataframe(self) -> DataFrame:
        return DataFrame([self.model_dump()])
    
    def to_numpy(self) -> ndarray:
        return self.to_dataframe().to_numpy()
