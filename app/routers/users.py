from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.schemas.user import AvatarUpdate, UserRead
from app.services.auth import get_current_user
from app.services.avatar import upload_avatar_to_cloudinary
from app.services.rate_limit import rate_limiter
from app.services.users import update_avatar

router = APIRouter()


@router.get("/me", response_model=UserRead, dependencies=[Depends(rate_limiter)])
async def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user


@router.patch("/avatar", response_model=UserRead)
async def update_avatar_from_data(
    avatar_data: AvatarUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await update_avatar(avatar_data, db, current_user)


@router.post("/avatar", summary="Upload or update avatar")
async def upload_avatar(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    url = await upload_avatar_to_cloudinary(
        file,
        public_id=f"user_avatars/{current_user.id}",
    )
    current_user.avatar = url
    db.add(current_user)
    await db.commit()
    return {"avatar_url": url}
