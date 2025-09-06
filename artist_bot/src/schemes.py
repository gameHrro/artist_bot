from pydantic import BaseModel

class AddNewIdea(BaseModel):
    name: str