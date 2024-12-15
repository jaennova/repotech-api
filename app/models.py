from sqlalchemy import Column, Integer, String, ARRAY, ForeignKey, DateTime, func
from app.database import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    image = Column(String)
    url = Column(String, nullable=False)
    tags = Column(ARRAY(String))
    status = Column(String, default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    icon = Column(String)
    tags = Column(ARRAY(String))
    parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True)