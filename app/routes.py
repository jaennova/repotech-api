from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List
from app.database import get_db
from app.models import Recurso, Tag
from app.schemas import RecursoCreate, RecursoResponse, TagResponse

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Bienvenido a la API de recursos"}

@router.post("/recursos/", response_model=RecursoResponse)
def create_resource(recurso: RecursoCreate, db: Session = Depends(get_db)):
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

@router.get("/recursos/", response_model=List[RecursoResponse])
def get_resources(db: Session = Depends(get_db)):
    try:
        recursos = db.query(Recurso).all()
        return recursos
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Error al obtener los recursos"
        )

@router.delete("/recursos/{recurso_id}")
def delete_resource(recurso_id: int, db: Session = Depends(get_db)):
    try:
        recurso = db.query(Recurso).filter(Recurso.id == recurso_id).first()
        if not recurso:
            raise HTTPException(
                status_code=404,
                detail="Recurso no encontrado"
            )
        db.delete(recurso)
        db.commit()
        return {"message": "Recurso eliminado exitosamente"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Error al eliminar el recurso"
        )

@router.get("/tags/", response_model=List[TagResponse])
def get_tags(db: Session = Depends(get_db)):
    try:
        tags = db.query(Tag).all()
        return tags
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Error al obtener los tags"
        )

@router.delete("/tags/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    try:
        tag = db.query(Tag).filter(Tag.id == tag_id).first()
        if not tag:
            raise HTTPException(
                status_code=404,
                detail="Tag no encontrado"
            )
        db.delete(tag)
        db.commit()
        return {"message": "Tag eliminado exitosamente"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Error al eliminar el tag"
        )

@router.get("/recursos/{recurso_id}", response_model=RecursoResponse)
def get_tag_by_id(recurso_id: int, db: Session = Depends(get_db)):
    try:
        recurso = db.query(Recurso).filter(Recurso.id == recurso_id).first()
        if not recurso:
            raise HTTPException(
                status_code=404,
                detail="Recurso no encontrado"
            )
        return recurso
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Error al obtener el recurso"
        )