from sqlmodel import create_engine, SQLModel

DATABASE_URL = "postgresql://postgres:senha@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

def get_db():
    with Session(engine) as session:
        yield session
