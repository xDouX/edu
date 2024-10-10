from fastapi import APIRouter, Depends
from random import randint
from schemas import TrainSchema, CreateInfo
from database import get_db, Session
from models import UserOrm

api_router = APIRouter()


@api_router.get("/hello")
def hello():
    return {"name": "Danil"}


@api_router.get("/random")
def random():
    return randint(1, 1000)


@api_router.post("/styled")
def styled(input_data: TrainSchema):
    first_name = input_data.first_row
    second_name = input_data.second_row

    return {"new_row": f"first string {first_name} + second string {second_name} = {first_name + second_name}"}


@api_router.post("/info")
def create_info(input_info: CreateInfo, session: Session = Depends(get_db)):
    new_info = UserOrm(name=input_info.name, surname=input_info.surname, age=input_info.age)
    session.add(new_info)
    session.commit()
    session.refresh(new_info)
    return {"message": f"User '{new_info.name}' inserted successfully"}


@api_router.get("/info/{get_name}")
def get_info(get_name: str, session: Session = Depends(get_db)):
    query = session.get(UserOrm, {"name": get_name})

    if query is None:
        return {"massage": "User not found"}

    return {
        "name": query.name,
        "surname": query.surname,
        "age": query.age
    }


@api_router.post("/delete/{get_name}")
def delete_info(get_name: str, session: Session = Depends(get_db)):
    user_to_delete = session.get(UserOrm, {"name": get_name})
    session.delete(user_to_delete)
    session.commit()

    if user_to_delete is None:
        return {"massage": "User not found"}

    return {
        "massage": f"User '{get_name}' deleted successfully"
    }
