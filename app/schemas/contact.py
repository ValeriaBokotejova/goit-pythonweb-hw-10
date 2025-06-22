from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class ContactBase(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    email: EmailStr
    phone_number: str = Field(..., max_length=20)
    birth_date: Optional[date] = None
    extra_info: Optional[str] = Field(None, max_length=250)


class ContactCreate(ContactBase):
    pass


class ContactUpdate(BaseModel):
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = Field(None, max_length=20)
    birth_date: Optional[date] = None
    extra_info: Optional[str] = Field(None, max_length=250)


class ContactRead(ContactBase):
    id: int

    class Config:
        orm_mode = True
