from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return {"hello","world"}


@app.post("/items/")
def create_item(name: str, price:float):
    return {"name": name, "price": price}

@app.put("items/{item_id}")
def update_item(item_id-id: int, name: str, price: float):
    return {"item_id": int, "name": str, "price":float}