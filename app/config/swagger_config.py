# app/config/swagger_config.py
import os

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Core LendingFront API",
        "description": "API para evaluar solicitudes de préstamo y futuras operaciones financieras.",
        "version": "0.0.03"
    },
    "host": os.getenv("SWAGGER_HOST", "localhost:5100"),
    "basePath": "/",
    "schemes": ["http"],
    "consumes": ["application/json"],
    "produces": ["application/json"],
    "tags": [
        {"name": "Loans", "description": "Operaciones relacionadas con préstamos"},
        {"name": "Users", "description": "Gestión de usuarios"}
    ]
}
