from fastapi import APIRouter

from app.routers import contacts, users

# Main API router that includes all sub-routers
router = APIRouter()
router.include_router(users.router, prefix="/auth", tags=["Auth"])
router.include_router(contacts.router, prefix="/contacts", tags=["Contacts"])
