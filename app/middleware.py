from fastapi.middleware.cors import CORSMiddleware

def setup_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["https://repotech.vercel.app", "http://localhost:4321"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )