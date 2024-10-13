from fastapi import APIRouter, Depends
from random import randint

from sqlalchemy import select

from schemas import TrainSchema, CreateInfo, CreateItem
from database import get_db, Session
from models import UserOrm, ItemsOrm

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


@api_router.get("/get_info/{get_name}")
def get_info(user_id: int, session: Session = Depends(get_db)):
    query = session.get(UserOrm, {"name": user_id})

    return {
        "name": query.name,
        "surname": query.surname,
        "age": query.age
    }


@api_router.delete("/delete/{get_name}")
def delete_info(user_id: int, session: Session = Depends(get_db)):
    user_to_delete = session.get(UserOrm, {"id": user_id})
    session.delete(user_to_delete)
    session.commit()

    return {
        "massage": f"User '{user_to_delete.name}' deleted successfully"
    }


@api_router.post("/items")
def create_item(give_item: CreateItem, session: Session = Depends(get_db)):
    new_item = ItemsOrm(name=give_item.name, user_id=give_item.user_id)
    session.add(new_item)
    session.commit()
    session.refresh(new_item)

    return {"message": f"Item '{new_item.name}' inserted successfully to User with id '{new_item.user_id}'"}


@api_router.get("/user_items/{user_name}")
def three_user_items(user_id: int, session: Session = Depends(get_db)):
    user = session.get(UserOrm, {"id": user_id})
    items = user.items

    if len(user.items) >= 3:
        return {
            "Selected User": f"{user.name} {user.surname} {user.age}",
            "first 3 items": f"{user.name} have {user.items[0].name, user.items[1].name, user.items[2].name}"
        }
    return {
        "message": "User has less then 3 items"
    }
