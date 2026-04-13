from fastapi import FastAPI

post1=FastAPI()

@post1.post("/items/")
def create_item(name: str, price: float):
    return {"name": name, "price": price}


