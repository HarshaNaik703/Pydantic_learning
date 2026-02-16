from pydantic import BaseModel
from typing import Field, Optional

# Todo : create product model with id, name, price, in_stock


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


input_model = {"id": 0, "name": "harsha", "price": 0.0}

product = Product(**input_model)

print(product)


class Employee(BaseModel):
    id: int
    name: str = Field(..., min_lenght=3, max_length=50, description = "Employee Name", example = "Harsha Naik")
    department : Optional[str] = 'General'
    salary : float = Field(...,ge=10000)
