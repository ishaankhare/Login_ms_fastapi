from datetime import date
from pydantic import BaseModel


class usersAuth(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True