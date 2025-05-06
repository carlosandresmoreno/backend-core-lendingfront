from pydantic import ValidationError
from flask import Blueprint, request, jsonify
from app.models.user import User
from app.schemas.user_schema import UserSchema
from app.extensions import db
from werkzeug.security import generate_password_hash

# Definir el Blueprint para usuarios
user_blueprint = Blueprint('user', __name__)

# Crear un esquema de usuario para la serialización y validación
user_schema = UserSchema()
users_schema = UserSchema(many=True)  # Para obtener una lista de usuarios

# Ruta para crear un nuevo usuario
@user_blueprint.route('/register', methods=['POST'])
def register_user():
    # Obtener datos de la solicitud
    input_data = request.get_json()

    # Validar y deserializar los datos de entrada
    try:
        user_data = user_schema.load(input_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Verificar si el correo electrónico ya existe
    if User.query.filter_by(email=user_data['email']).first():
        return jsonify({"message": "El correo electrónico ya está registrado."}), 400

    # Crear el nuevo usuario
    new_user = User(
        email=user_data['email'],
        first_name=user_data['first_name'],
        last_name=user_data['last_name'],
        password=generate_password_hash(user_data['password']),
    )

    # Guardar el usuario en la base de datos
    db.session.add(new_user)
    db.session.commit()

    # Serializar el usuario y devolver la respuesta
    return jsonify(user_schema.dump(new_user)), 201

# Ruta para obtener la información de un usuario
@user_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user_schema.dump(user))

# Ruta para actualizar los datos de un usuario
@user_blueprint.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)

    # Obtener los nuevos datos desde la solicitud
    input_data = request.get_json()

    try:
        user_data = user_schema.load(input_data, partial=True)  # Los datos no necesitan ser completos
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Actualizar el usuario con los nuevos datos
    if 'email' in user_data:
        user.email = user_data['email']
    if 'first_name' in user_data:
        user.first_name = user_data['first_name']
    if 'last_name' in user_data:
        user.last_name = user_data['last_name']
    if 'password' in user_data:
        user.password = generate_password_hash(user_data['password'])

    # Guardar los cambios en la base de datos
    db.session.commit()

    return jsonify(user_schema.dump(user))

# Ruta para eliminar un usuario
@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuario eliminado"}), 200
