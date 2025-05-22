from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, nullable=False)
    email: str = Field(unique=True, nullable=False)
    password: str = Field(nullable=False)

    tasks: List["Task"] = Relationship(back_populates="owner")
