from pydantic import BaseModel

class signInBody(BaseModel):
    username: str
    password: str