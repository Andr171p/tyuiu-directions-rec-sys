from pydantic import BaseModel


class DirectionSchema(BaseModel):
    number: str
    name: str
    link: str
