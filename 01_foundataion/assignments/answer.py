from pydantic import BaseModel

# Todo : create product model with id, name, price, in_stock

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool = True

input_model = {'id' : 0, 'name' : 'harsha', 'price' : 0.0}

product = Product(**input_model)

print(product)



