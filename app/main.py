from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import router
from app.middleware import setup_cors_middleware

app = FastAPI(title="Tech Resources API")

# Configurar el middleware CORS
setup_cors_middleware(app)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir las rutas
app.include_router(router)