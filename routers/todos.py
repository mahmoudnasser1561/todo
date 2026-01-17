from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from database import SessionLocal
from starlette import status
from models import Todos

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/")
async def read_all(db: Annotated[Session, Depends(get_db)]):
    return db.query(Todos).all()

@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id)
    if todo_model is not None:
        return todo_model
    raise HTTPException(session_code=404, detail="todo not found.")