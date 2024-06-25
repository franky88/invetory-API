from typing import Union
from fastapi import FastAPI, status

from . import crud, models, schemas
from app.database import engine
from app.models import Base
from app.routers import users

# models.Base.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {"Hello": "World"}

# @app.get("/sample")
# def sample():
#     return {"Hello": "from sample"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.get("/files/{file_path:path}")
# def read_file(file_path: str):
#     return {"file_path": file_path}