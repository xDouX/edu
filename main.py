from fastapi import FastAPI
from router import api_router
from database import engine, Base
import uvicorn

app = FastAPI()

app.include_router(api_router)

Base.metadata.create_all(engine)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

