from pydantic import BaseModel
from datetime import date
from typing import Optional
from typing import List


class User(BaseModel):
    username:str
    password:str

class UserResponse(BaseModel):
    id:int
    username:str
    posts:Optional[List["PostResponse"]]


class Post(BaseModel):
    game_id:int
    creation_date:date
    user_id:int


class PostResponse(BaseModel):
    id:int
    game_id:int
    creation_date:date
    user_id:int


class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username: Optional[str] = None