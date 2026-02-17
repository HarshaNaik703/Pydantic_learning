from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street : str
    city : str
    pincode : str

class User(BaseModel):
    id : int
    name : str
    email : str
    is_active : bool = True
    created_at : datetime
    address : Address
    tags : List[str] = []


    model_config = ConfigDict(
        json_encoders={datetime : lambda v : v.strftime(
            '%d-%m-%Y %H-%M-%S'
        )}
    )

# create a user instance

user = User(
    id = 1, 
    name = 'Harhsa', 
    email = "harshanaik@gmail.com", 
    created_at=datetime.now(),
    address= Address(
        street="Konalli",
        city= "Kumta",
        pincode="541323"
    ),
    tags= ["premium", "subscriber"]
)

print(user)
print()
python_dict = user.model_dump()
print(python_dict)
print()
python_dict = user.model_dump_json()

print(python_dict)
