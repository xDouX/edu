from pydantic import BaseModel


class CreateInfo(BaseModel):
    name: str
    surname: str
    age: int
    user_group: str


class CreateItem(BaseModel):
    name: str
    weight: float
    description: str
    users_id: int
