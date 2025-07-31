from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    age: int

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title: str 
    body: str
    author_id: int

class PostResponse(PostBase):
    id: int
    author: User

    class Config:
        orm_mode = True

class PostCreate(PostBase):
    pass
