from src.schemas import ApplicantSchema, ExamSchema
from src.schemas.vector import VectorSchema


exam = ExamSchema(
    name="math",
    points=76
)

applicant = ApplicantSchema(
    gender="male",
    foreign_citizenship="Russian",
    military_service="yes",
    gpa=4.2,
    points=227,
    bonus_points=10,
    exams=[exam]
)

print(applicant.exams_dict)
vector = VectorSchema.from_applicant(applicant)
print(vector.to_dataframe())
print(vector.to_numpy())