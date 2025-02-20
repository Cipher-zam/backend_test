from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, status
from database import getDB
from models.models import PostModel
from schemas.schemas import Post, PostResponse
from typing import List

router = APIRouter(
    prefix= "/posts",
    tags=['Posts']
)

@router.get("/", response_model=List[PostResponse])
def get_all(db:Session=Depends(getDB)):
    posts = db.query(PostModel).all()

    return posts

@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create(request:Post,db:Session=Depends(getDB)):
    newPost = PostModel(game_id=request.game_id, creation_date=request.creation_date, user_id=request.user_id)
    db.add(newPost)
    db.commit()
    db.flush(newPost)

    return newPost