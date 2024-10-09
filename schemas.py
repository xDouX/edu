from pydantic import BaseModel


class TrainSchema(BaseModel):
    first_row: str
    second_row: str


class CreateInfo(BaseModel):
    name: str
    surname: str
    age: int
