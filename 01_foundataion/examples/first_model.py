from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active : bool

input_data = {'id' : 101,  'is_active':True,'name' : 'Chaicode'}

user = User(**input_data)

print(user)
