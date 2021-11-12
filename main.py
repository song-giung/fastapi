from enum import Enum
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, "item_id": item_id}


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep LEARNING FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all teh images"}

    return {"model_name": model_name, "message": "have some residuals"}


# if path parameter containing paths
# like .. /files/myhome/work/awesome_python.txt
@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {"file_path": file_path}


fake_items_db = [
    {"item_name": "foo"},
    {"item_name": "bar"},
    {"item_name": "baz"}
]


@app.get('/items/')
async def read_items(skip: int = 0, limit: int = 0):
    return fake_items_db[skip:skip + limit]
