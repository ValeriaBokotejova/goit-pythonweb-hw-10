from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

from app.config import settings

# Define the base class for all SQLAlchemy models
Base = declarative_base()

# Create an asynchronous SQLAlchemy engine using the database URL from settings
engine: AsyncEngine = create_async_engine(settings.database_url, echo=True)

# Create a session factory for asynchronous database sessions
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


# Dependency for FastAPI routes that provides a database session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
