from fastapi import FastAPI  # import FastAPI class
from typing import Union

app = FastAPI()  # instance of FastAPI class


@app.get("/")  # decorator
def read_root():  # function
    return {"Hello": "World"}

# get, post, put, delete, options, head, patch and trace are the methods supported by FastAPI

#


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
