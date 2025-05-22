from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.crud import task as crud_task
from typing import List
from app.services.auth_service import get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=TaskOut)
def create(task: TaskCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return crud_task.create_task(db, task)

@router.get("/{task_id}", response_model=TaskOut)
def read(task_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    task = crud_task.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/", response_model=List[TaskOut])
def list_by_user(assignedTo: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return crud_task.get_tasks_by_user(db, assignedTo)

@router.put("/{task_id}", response_model=TaskOut)
def update(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    task = crud_task.update_task(db, task_id, task_update)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    task = crud_task.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
