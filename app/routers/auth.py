from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.auth import TokenResponse, UserCreate, UserLogin
from app.services.auth import authenticate_user, register_user

router = APIRouter()


@router.post(
    "/signup",
    response_model=TokenResponse,
    status_code=status.HTTP_201_CREATED,
)
async def signup(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    return await register_user(user_data, db)


@router.post("/login", response_model=TokenResponse)
async def login(user_data: UserLogin, db: AsyncSession = Depends(get_db)):
    return await authenticate_user(user_data, db)
