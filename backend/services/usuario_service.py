from flask import Blueprint, request, jsonify
from data_access.access.usuario_repository import UsuarioRepository
from connection.db_config import db
import bcrypt

usuario_bp = Blueprint('usuario_bp', __name__)

# Función para serializar objetos Usuario
def usuario_to_dict(usuario):
    return {
        "id_usuario": usuario.id_usuario,
        "nombre": usuario.nombre,
        "email": usuario.email,
        "rol": usuario.rol
    }

# Obtener todos los usuarios
@usuario_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    dao = UsuarioRepository(db)
    usuarios = dao.get_all_usuarios()
    return jsonify([usuario_to_dict(u) for u in usuarios])

# Obtener un usuario por ID
@usuario_bp.route('/usuarios/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    dao = UsuarioRepository(db)
    usuario = dao.get_usuario(usuario_id)
    return jsonify(usuario_to_dict(usuario)) if usuario else (jsonify({"error": "Usuario no encontrado"}), 404)

# Obtener un usuario por email
@usuario_bp.route('/usuarios/email/<string:email>', methods=['GET'])
def get_usuario_por_email(email):
    dao = UsuarioRepository(db)
    usuario = dao.get_usuario_por_email(email)
    return jsonify(usuario_to_dict(usuario)) if usuario else (jsonify({"error": "Usuario no encontrado"}), 404)

# Crear un nuevo usuario
@usuario_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    if not all(k in data for k in ("nombre", "email", "contrasena_hash", "rol")):
        return jsonify({"error": "Faltan campos requeridos"}), 400

    # Hashear la contraseña antes de guardarla
    hashed_password = bcrypt.hashpw(data['contrasena_hash'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    dao = UsuarioRepository(db)
    usuario = dao.create_usuario(data['nombre'], data['email'], hashed_password, data['rol'])
    
    return jsonify(usuario_to_dict(usuario)), 201

# Actualizar usuario
@usuario_bp.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def update_usuario(usuario_id):
    data = request.json
    if not all(k in data for k in ("nombre", "email", "contrasena_hash", "rol")):
        return jsonify({"error": "Faltan campos requeridos"}), 400

    hashed_password = bcrypt.hashpw(data['contrasena_hash'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    dao = UsuarioRepository(db)
    usuario = dao.update_usuario(usuario_id, data['nombre'], data['email'], hashed_password, data['rol'])

    return jsonify(usuario_to_dict(usuario)) if usuario else (jsonify({"error": "Usuario no encontrado"}), 404)

# Eliminar usuario
@usuario_bp.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    dao = UsuarioRepository(db)
    usuario = dao.delete_usuario(usuario_id)
    return jsonify({"message": "Usuario eliminado"}) if usuario else (jsonify({"error": "Usuario no encontrado"}), 404)
