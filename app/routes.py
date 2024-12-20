from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List
from app.database import get_db
from app.models import Recurso, Tag
from app.schemas import RecursoCreate, RecursoResponse, TagResponse

router = APIRouter()

@router.post("/recursos/", response_model=RecursoResponse)
def create_recurso(recurso: RecursoCreate, db: Session = Depends(get_db)):
    try:
        # Verificar si ya existe un recurso con el mismo título
        existing_recurso = db.query(Recurso).filter(Recurso.titulo == recurso.titulo).first()
        if existing_recurso:
            raise HTTPException(
                status_code=400,
                detail="Ya existe un recurso con este título"
            )

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

    except IntegrityError as e:
        db.rollback()
        if "recursos_titulo_key" in str(e):
            raise HTTPException(
                status_code=400,
                detail="Ya existe un recurso con este título"
            )
        raise HTTPException(
            status_code=400,
            detail="Error de integridad en la base de datos"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Error interno del servidor"
        )
