from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class users_auth(Base):
    __tablename__ = "users_auth"

    username = Column(String, primary_key=True)
    password = Column(String)

