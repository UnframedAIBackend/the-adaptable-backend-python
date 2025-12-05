from typing import Union
from pydantic import BaseModel, Field

class Note(BaseModel):
    id: Union[int, str] = Field(..., example=1)
    content: str = Field(..., example="Hello World")
