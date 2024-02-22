from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from enum import Enum




class SortEnum(Enum):
    earliest = "earliest"
    latest = "latest"


class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Task(BaseModel):
    content: str
    deadline: Optional[datetime] = None
    priority: PriorityEnum
    completed: Optional[bool] = False

class TaskOut(Task):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class TaskDeleteOut(BaseModel):
    id: int
    owner_id: int
    deleted_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserUpdate(UserCreate):
    pass

class UserOut(BaseModel):
    id: int
    email: str
    username: str
    created_at: datetime

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    data: UserOut
    message: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None


class JWTVerifyResponse(BaseModel):
    data: UserOut
    message: str