from fastapi import FastAPI
from app.routers import auth
from app.routers import task
from app.routers import users 

app = FastAPI()

app.include_router(users.router, prefix="/api/users")
app.include_router(task.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
	return {"message": "API Task Manager funcionando!"}
