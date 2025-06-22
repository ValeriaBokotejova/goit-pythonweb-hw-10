from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.schemas.user import AvatarUpdate, UserRead
from app.services.auth import get_current_user
from app.services.rate_limit import rate_limiter
from app.services.users import update_avatar

router = APIRouter()


@router.get("/me", response_model=UserRead, dependencies=[Depends(rate_limiter)])
async def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user


@router.patch("/avatar", response_model=UserRead)
async def change_avatar(
    avatar_data: AvatarUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await update_avatar(avatar_data, db, current_user)
