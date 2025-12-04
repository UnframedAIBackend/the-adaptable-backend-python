from pydantic import BaseModel, Field

class NoteDto(BaseModel):
    id: int = Field(..., example=1)
    content: str = Field(..., example="Hello World")
