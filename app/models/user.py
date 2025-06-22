from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    avatar = Column(String, nullable=True)
    is_verified = Column(Boolean, default=False)
    avatar = Column(String, nullable=True)

    # Relationship to contacts
    contacts = relationship("Contact", back_populates="owner", cascade="all, delete")
