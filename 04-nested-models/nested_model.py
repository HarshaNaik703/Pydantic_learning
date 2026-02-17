from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street : str
    city : str
    postal_code : str


class User(BaseModel):
    id : int
    name : str
    address : Address

class Comment(BaseModel):
    id : int
    content : str
    replies : Optional[List['Comment']] = None

Comment.model_rebuild()
