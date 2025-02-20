from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Date
from sqlalchemy.orm import relationship


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)

    posts = relationship("PostModel", back_populates="user")


class PostModel(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer)
    creation_date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("UserModel", back_populates="posts")