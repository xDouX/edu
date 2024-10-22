from fastapi import APIRouter, Depends

from sqlalchemy import update

from schemas import CreateInfo, CreateItem
from database import get_db, Session
from models import UserOrm, ItemsOrm, WorkGroup

api_router = APIRouter()


@api_router.post("/group")
def create_group(group_name: str, session: Session = Depends(get_db)):
    new_group = WorkGroup(name=group_name)
    session.add(new_group)
    session.commit()

    return {"message": "Success"}


@api_router.get("/get_group_info")
def get_info_by_group(group: str, session: Session = Depends(get_db)):
    work_group = session.get(WorkGroup, {"name": group})
    print(work_group.users)
    return {
        "group_name": work_group.name,
        "users": [
            {
                "id": user.id,
                "name": user.name,
                "surname": user.surname,
                "age": user.age,
                "items": user.items
            }
            for user in work_group.users
        ]
    }


@api_router.post("/info")
def create_info(input_info: CreateInfo, session: Session = Depends(get_db)):
    new_info = UserOrm(
        name=input_info.name,
        surname=input_info.surname,
        age=input_info.age,
        user_group=input_info.user_group
    )
    session.add(new_info)
    session.commit()
    session.refresh(new_info)

    return {"message": f"User '{new_info.name}' inserted successfully"}


@api_router.get("/get_info/{get_name}")
def get_info(user_id: int, session: Session = Depends(get_db)):
    query = session.get(UserOrm, {"id": user_id})

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
    new_item = (ItemsOrm(
        name=give_item.name,
        weight=give_item.weight,
        description=give_item.description,
        users_id=give_item.users_id
    ))
    session.add(new_item)
    session.commit()
    session.refresh(new_item)

    return {"message": f"Item '{new_item.name}' inserted successfully to User with id '{new_item.users_id}'"}


@api_router.get("/user_items/{user_name}")
def three_user_items(user_id: int, session: Session = Depends(get_db)):
    user = session.get(UserOrm, {"id": user_id})
    items = user.items

    if len(user.items) >= 3:
        return {
            "Selected User": {
                "Name": user.name,
                "Surname": user.surname,
                "Age": user.age
            },
            "first 3 items": {
                "item 1": {
                    "item name": items[0].name,
                    "items weight": items[0].weight,
                    "items description": items[0].description
                },
                "item 2": {
                    "item name": items[1].name,
                    "items weight": items[1].weight,
                    "items description": items[1].description
                },
                "item 3": {
                    "item name": items[2].name,
                    "items weight": items[2].weight,
                    "items description": items[2].description
                },
            }
        }
    return {"message": "User has less then 3 items"}


@api_router.patch("/trade_items")
def trade_items(items_id: int, transfer_to_user: int, session: Session = Depends(get_db)):
    stmt = (
        update(ItemsOrm).
        values(users_id=transfer_to_user).
        filter_by(id=items_id)
    )
    session.execute(stmt)
    session.commit()
    res = session.get(UserOrm, {"id": transfer_to_user})
    return {
        "Items": res.items.name
    }


@api_router.patch("/patch_items")
def patch_items(item_id: int, item_name: str, session: Session = Depends(get_db)):
    stmt = (
        update(ItemsOrm).
        values(name=item_name).
        filter_by(id=item_id)
    )
    session.execute(stmt)
    session.commit()
    return {
        "message": "Success"
    }

