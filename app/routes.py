from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Recurso, Tag
from app.schemas import RecursoCreate, RecursoResponse, TagResponse

router = APIRouter()

@router.post("/recursos/", response_model=RecursoResponse)
def create_recurso(recurso: RecursoCreate, db: Session = Depends(get_db)):
    # Crear el recurso
    db_recurso = Recurso(
        titulo=recurso.titulo,
        descripcion=recurso.descripcion,
        url=recurso.url
    )
    
    # Procesar tags
    for tag_nombre in recurso.tags:
        # Buscar o crear tag
        tag = db.query(Tag).filter(Tag.nombre == tag_nombre).first()
        if not tag:
            tag = Tag(nombre=tag_nombre)
            db.add(tag)
        db_recurso.tags.append(tag)
    
    db.add(db_recurso)
    db.commit()
    db.refresh(db_recurso)
    return db_recurso

@router.get("/recursos/", response_model=List[RecursoResponse])
def read_recursos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    recursos = db.query(Recurso).offset(skip).limit(limit).all()
    return recursos

@router.get("/recursos/{recurso_id}", response_model=RecursoResponse)
def read_recurso(recurso_id: int, db: Session = Depends(get_db)):
    recurso = db.query(Recurso).filter(Recurso.id == recurso_id).first()
    if recurso is None:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")
    return recurso

@router.get("/tags/", response_model=List[TagResponse])
def read_tags(db: Session = Depends(get_db)):
    tags = db.query(Tag).all()
    return tags