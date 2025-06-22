from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.schemas.contact import ContactCreate, ContactRead, ContactUpdate
from app.services.auth import get_current_user
from app.services.contacts import (
    create_contact,
    delete_contact,
    get_contact_by_id,
    get_contacts,
    get_upcoming_birthdays,
    update_contact,
)

router = APIRouter()


@router.post("/", response_model=ContactRead, status_code=status.HTTP_201_CREATED)
async def create_contact_view(
    contact: ContactCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await create_contact(contact, db, current_user)


@router.get("/", response_model=List[ContactRead])
async def list_contacts(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await get_contacts(db, current_user)


@router.get("/upcoming/birthdays", response_model=List[ContactRead])
async def upcoming_birthdays(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await get_upcoming_birthdays(db, current_user)


@router.get("/{contact_id}", response_model=ContactRead)
async def get_contact_view(
    contact_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await get_contact_by_id(contact_id, db, current_user)


@router.put("/{contact_id}", response_model=ContactRead)
async def update_contact_view(
    contact_id: int,
    contact_data: ContactUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await update_contact(contact_id, contact_data, db, current_user)


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact_view(
    contact_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await delete_contact(contact_id, db, current_user)
