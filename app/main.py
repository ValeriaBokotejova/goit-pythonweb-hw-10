from fastapi import FastAPI

from app.database import Base, engine
from app.middleware.cors import configure_cors
from app.routers import auth, contacts

# Initialize FastAPI app
app = FastAPI(
    title="Contacts API",
    description="A RESTful API for managing contacts with authentication and avatar support.",
    version="1.0.0",
)

# Setup CORS middleware
configure_cors(app)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(contacts.router, prefix="/api/contacts", tags=["Contacts"])


# Create tables if not using migrations (optional)
# You can remove this in production and rely on Alembic
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
