from pydantic import BaseModel
from typing import Optional, List

#todo create course model
# each course has modules
# each modules has lessoins

class Lession(BaseModel):
    lession_id : int
    topic : str

class Module(BaseModel):
    module_id : int
    name : str
    lessoins : List[Lession]

class Course(BaseModel):
    course_id : id
    title : str
    modules : List[Module]
