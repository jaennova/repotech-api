# API de Recursos Tecnológicos

## Descripción
API REST construida con FastAPI para gestionar recursos tecnológicos y sus tags asociados. La API permite crear, listar, buscar y eliminar recursos y tags, utilizando SQLAlchemy para la gestión de base de datos y Pydantic para la validación de datos.

## Estructura del Proyecto
```
repotech-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   └── middleware.py
├── .env
├── requirements.txt
└── .gitignore
```

## Tecnologías Principales
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- Uvicorn
- Gunicorn (para producción)

## Requisitos
- Python 3.7 o superior
- PostgreSQL

## Instalación
1. Clonar el repositorio:
```bash
git clone https://github.com/jaennova/repotech-api.git
cd repotech-api
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
Crear archivo `.env` en la raíz del proyecto:
```
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombrebd
```

## Ejecución
### Desarrollo
```bash
uvicorn app.main:app --reload
```

### Producción
```bash
gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
```

## Endpoints de la API

### Recursos
- **GET /**: Mensaje de bienvenida
- **POST /recursos/**: Crear nuevo recurso
- **GET /recursos/**: Obtener lista de recursos
- **GET /recursos/{recurso_id}**: Obtener recurso por ID
- **DELETE /recursos/{recurso_id}**: Eliminar recurso por ID
- **DELETE /recursos/nombre/{titulo}**: Eliminar recurso por título
- **GET /recursos/buscar/**: Buscar recursos con filtros y paginación
  - Parámetros opcionales:
    - q: término de búsqueda
    - tag: filtrar por tag
    - skip: número de registros a saltar
    - limit: límite de registros por página

### Tags
- **GET /tags/**: Obtener lista de tags
- **DELETE /tags/{tag_id}**: Eliminar tag por ID
- **DELETE /tags/nombre/{nombre}**: Eliminar tag por nombre

## Modelos de Datos

### Recurso
```json
{
  "titulo": "string",
  "descripcion": "string",
  "url": "string",
  "tags": ["string"]
}
```

### Tag
```json
{
  "id": "integer",
  "nombre": "string"
}
```

## Características
- CORS habilitado para integración con frontend (repotech.vercel.app y localhost:4321)
- Búsqueda y filtrado de recursos
- Paginación de resultados
- Manejo de errores personalizado
- Validación de datos con Pydantic
- Soporte para PostgreSQL
- Documentación automática (Swagger UI)

## Ejemplo de Búsqueda y Paginación
```
GET /recursos/buscar/?q=python&tag=backend&skip=0&limit=10
```
Respuesta:
```json
{
    "total": 100,
    "recursos": [],
    "skip": 0,
    "limit": 10
}
```

## Documentación API
La documentación interactiva está disponible en:
- Swagger UI: `/docs`
- ReDoc: `/redoc`

## Despliegue
La API está desplegada en Render y utiliza una base de datos PostgreSQL.
