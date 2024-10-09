from fastapi import APIRouter
from random import randint
from schemas import TrainSchema, CreateInfo
from make_db import get_db_connection

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
def create_info(input_info: CreateInfo):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO my_info (name, surname, age) VALUES (?, ?, ?)",
        (input_info.name, input_info.surname, input_info.age)
    )
    conn.commit()
    conn.close()
    return {"message": "Data inserted successfully"}


@api_router.get('/info/{info_id}')
def get_info(info_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM my_info WHERE id=?",
        (info_id,)
    )
    info = cursor.fetchone()
    conn.close()
    return {
        "id": info["id"],
        "name": info["name"],
        "surname": info["surname"],
        "age": info["age"]
    }
