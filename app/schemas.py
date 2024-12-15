from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ResourceBase(BaseModel):
    title: str
    description: str
    image: Optional[str] = None
    url: str
    tags: List[str]
    status: str = "pending"

class ResourceCreate(ResourceBase):
    pass

class ResourceResponse(ResourceBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name: str
    icon: str
    tags: List[str]
    parent_id: Optional[int] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True