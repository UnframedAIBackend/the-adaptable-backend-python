from pydantic import BaseModel, Field

class Note(BaseModel):
    id: int = Field(..., example=1)
    content: str = Field(..., example="Hello World")
