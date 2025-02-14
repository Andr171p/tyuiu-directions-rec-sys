from typing import List, Literal

from pandas import DataFrame

from pydantic import BaseModel

from src.schemas.exam import ExamSchema


class ApplicantSchema(BaseModel):
    gender: Literal['М', 'Ж']
    foreign_citizenship: str
    military_service: Literal["да", "нет"]
    gpa: float
    points: int
    bonus_points: int
    exams: List[ExamSchema]
    
    def to_dataframe(self) -> DataFrame:
        dumped_model = self.model_dump()
        exams = dumped_model.pop("exams")
        dataframe = DataFrame([dumped_model])
        for exam in exams:
            dataframe[exam["name"]] = exam["points"]
        return dataframe
