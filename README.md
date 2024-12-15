# API de Recursos Tecnológicos

## Descripción
Este proyecto es una API construida con FastAPI para gestionar recursos tecnológicos y sus categorías. Utiliza SQLAlchemy para la interacción con la base de datos y Pydantic para la validación de datos.

## Estructura del Proyecto
```
repotech-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── routes.py
│   └── schemas.py
├── .env
└── requirements.txt
```

### Archivos Principales
- **`main.py`**: Inicializa la aplicación FastAPI y define las rutas de la API
- **`database.py`**: Configura la conexión a la base de datos y gestiona las sesiones
- **`models.py`**: Define los modelos de datos usando SQLAlchemy
- **`schemas.py`**: Define los esquemas de validación de datos usando Pydantic
- **`routes.py`**: Contiene las definiciones de los endpoints de la API

## Requisitos
Asegúrate de tener Python 3.7 o superior instalado. Luego instala las dependencias del proyecto:
```bash
pip install -r requirements.txt
```

## Configuración
Crea un archivo `.env` en la raíz del proyecto y define tu URL de base de datos:
```
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombrebd
```

## Ejecutar la Aplicación
Para ejecutar la aplicación, usa el siguiente comando:
```bash
uvicorn app.main:app --reload
```
La API estará disponible en `http://localhost:8000` y la documentación interactiva en `http://localhost:8000/docs`.

## Endpoints de la API
- **GET /**: Obtener mensaje de bienvenida y lista de endpoints disponibles
- **POST /api/resources/**: Crear un nuevo recurso
- **GET /api/resources/**: Obtener lista de recursos
- **GET /api/resources/{resource_id}**: Obtener recurso específico por ID
- **POST /api/categories/**: Crear una nueva categoría
- **GET /api/categories/**: Obtener lista de categorías
- **GET /api/categories/{category_id}**: Obtener categoría específica por ID

## Contribuciones
Las contribuciones son bienvenidas. No dudes en abrir un issue o enviar un pull request.
