from datetime import datetime
from app.extensions import db
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, email, password, first_name=None, last_name=None):
        self.email = email
        self.set_password(password)
        self.first_name = first_name
        self.last_name = last_name

    def set_password(self, password):
        """Cifra la contraseña del usuario"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica si la contraseña ingresada coincide con la almacenada"""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.id}, {self.email}>'

    @staticmethod
    def is_email_unique(email):
        """Verifica si el correo electrónico es único en la base de datos"""
        return User.query.filter_by(email=email).first() is None
