
from fastapi.routing import APIRouter
from schemas.schemas import Token
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from database import getDB
from models.models import UserModel
import hash
from JWTToken import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/login",tags=['Login'])

@router.post("/", response_model=Token)
def login(request:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(getDB)):
    user = db.query(UserModel).filter(UserModel.username==request.username).first()

    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    
    if not hash.verfify(request.password, user.password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,"password wrong")
    
    access_token = create_access_token({"sub": user.username})
    return {"access_token":access_token, "token_type":"bearer"}