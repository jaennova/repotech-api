from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Resource, Category
from app.schemas import (
    ResourceCreate, 
    ResourceResponse, 
    CategoryCreate, 
    CategoryResponse
)

router = APIRouter()

@router.get("/")
def read_root():
    return {
        "message": "Welcome to Tech Resources API",
        "version": "1.0.0",
        "endpoints": {
            "resources": "/api/resources/",
            "categories": "/api/categories/"
        }
    }

# Endpoints para Resources
@router.post("/api/resources/", response_model=ResourceResponse)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    db_resource = Resource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

@router.get("/api/resources/", response_model=List[ResourceResponse])
def read_resources(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    resources = db.query(Resource).offset(skip).limit(limit).all()
    return resources

@router.get("/api/resources/{resource_id}", response_model=ResourceResponse)
def read_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

# Endpoints para Categories
@router.post("/api/categories/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/api/categories/", response_model=List[CategoryResponse])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = db.query(Category).offset(skip).limit(limit).all()
    return categories

@router.get("/api/categories/{category_id}", response_model=CategoryResponse)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category