from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    avatar: Optional[str] = None
    is_verified: bool

    class Config:
        from_attributes = True


class AvatarUpdate(BaseModel):
    avatar_url: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
