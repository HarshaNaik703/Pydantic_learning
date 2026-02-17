from pydantic import BaseModel, Field
from typing import Dict, List, Optional

# Todo: Create a Employee model (using fileds)


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Enter the name ",
        title="Name of the person",
        examples="Harsha Naik",
    )
    department = Optional[str] = "General"
    salary: float = Field(..., ge=10000)
