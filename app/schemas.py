from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum
class TagBase(BaseModel):
    nombre: str

class TagCreate(TagBase):
    pass

class TagResponse(TagBase):
    id: int

    class Config:
        from_attributes = True

class RecursoBase(BaseModel):
    titulo: str
    descripcion: str
    url: str

class RecursoCreate(RecursoBase):
    tags: List[str]

class RecursoResponse(RecursoBase):
    id: int
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    tags: List[TagResponse]

    class Config:
        from_attributes = True

class Ordenamiento(str, Enum):
    TITULO = "titulo"
    FECHA = "fecha"
    RECIENTE = "reciente"