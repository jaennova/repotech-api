from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

# Tabla intermedia para la relación muchos a muchos
recursos_tags = Table(
    'recursos_tags',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('recurso_id', Integer, ForeignKey('recursos.id', ondelete='CASCADE')),
    Column('tag_id', Integer, ForeignKey('tags.id', ondelete='CASCADE')),
    UniqueConstraint('recurso_id', 'tag_id', name='uq_recurso_tag')
)

class Recurso(Base):
    __tablename__ = "recursos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), unique=True, nullable=False, index=True)
    descripcion = Column(Text, nullable=False)
    url = Column(String(2048), nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relación muchos a muchos con Tags
    tags = relationship("Tag", secondary=recursos_tags, back_populates="recursos")

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False, index=True)
    
    # Relación muchos a muchos con Recursos
    recursos = relationship("Recurso", secondary=recursos_tags, back_populates="tags")