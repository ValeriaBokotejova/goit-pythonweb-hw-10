from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    """Schema for registering a new user"""

    username: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6)


class UserLogin(BaseModel):
    """Schema for logging in a user"""

    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """Schema for returning the access token"""

    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    """Schema for returning user data"""

    id: int
    username: str
    email: EmailStr
    avatar: str | None = None
    is_verified: bool

    class Config:
        orm_mode = True
