from src.schemas import ApplicantSchema, ExamSchema


math_exam = ExamSchema(
    name="Математика",
    points=90
)
russian_exam = ExamSchema(
    name="Русский язык",
    points=70
)
physics_exam = ExamSchema(
    name="Физика",
    points=67
)
applicant = ApplicantSchema(
    gender="М",
    foreign_citizenship="Россия",
    military_service="да",
    gpa=4.5,
    points=220,
    bonus_points=10,
    exams=[math_exam, russian_exam, physics_exam]
)
df = applicant.to_dataframe()
print(df)