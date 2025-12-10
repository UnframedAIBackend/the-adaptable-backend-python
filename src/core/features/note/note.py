from typing import Union
from pydantic import BaseModel, Field

class CreateNoteDto(BaseModel):
    content: str = Field(..., example="Hello World")

class UpdateNoteDto(CreateNoteDto):
    pass

class Note(CreateNoteDto):
    id: Union[int, str] = Field(..., example=1)
