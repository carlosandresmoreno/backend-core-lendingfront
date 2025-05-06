from .config import Config
import os

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI', 'postgresql://prod_user:password@localhost/prod_db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave_secreta_prod')
