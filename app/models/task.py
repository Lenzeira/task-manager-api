from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from app.models.user import User

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    completed: bool = Field(default=False)
    owner_id: int = Field(foreign_key="user.id")

    owner: Optional[User] = Relationship(back_populates="tasks")
