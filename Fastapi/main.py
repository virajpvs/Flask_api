# http://127.0.0.1:8000/docs -> Swagger UI

from fastapi import FastAPI  # import FastAPI class
from typing import Union

app = FastAPI()  # instance of FastAPI class


# decorator/ api decorator/ api route/ api endpoint/ api path operation decorator
@app.get("/")
def read_root():  # function
    return {"Hello": "World"}

# get, post, put, delete, options, head, patch and trace are the methods supported by FastAPI


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
