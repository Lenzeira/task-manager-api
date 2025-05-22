from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id, Task.deleted == False).first()

def get_tasks_by_user(db: Session, user_id: int):
    return db.query(Task).filter(Task.assigned_to == user_id, Task.deleted == False).all()

def update_task(db: Session, task_id: int, task_update: TaskUpdate):
    task = get_task(db, task_id)
    if not task:
        return None
    for key, value in task_update.dict(exclude_unset=True).items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    if not task:
        return None
    task.deleted = True
    db.commit()
    return task
