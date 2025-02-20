from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from database import getDB
from models.models import UserModel
from schemas.schemas import User, UserResponse
from typing import List,Optional
import oauth

router = APIRouter(
    prefix= "/users",
    tags=['Users']
)


def userExists(db:Session, username):
    user = db.query(UserModel).filter(UserModel.username == username).first()

    return user!=None


@router.get("/", response_model=List[UserResponse])
def get_all(db:Session=Depends(getDB), currentUser:User = Depends(oauth.get_current_user)):
    users = db.query(UserModel).all()

    return users

@router.get("/{id}")
def get(id:int, include:Optional[str]=None, db:Session=Depends(getDB)):
    user = db.query(UserModel).filter(UserModel.id == id).first()

    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,"User not found")
    
    response = {"id": user.id,"username":user.username}

    if include and "posts" in include.split(','):
        response["posts"] = user.posts

    return response

@router.get('/exists/{username}')
def exists(username,db:Session = Depends(getDB)):
    return "true" if userExists( db, username) else "false"


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create(request:User,db:Session=Depends(getDB)):

    if(userExists(db,request.username)):
        raise HTTPException(status.HTTP_302_FOUND, "User already exists")

    newUser = UserModel(username=request.username, password=request.password)
    db.add(newUser)
    db.commit()
    db.flush(newUser)

    return newUser