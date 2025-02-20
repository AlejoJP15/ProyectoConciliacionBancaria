from flask import Blueprint, request, jsonify
from data_access.access.validacion_repository import ValidacionRepository
from connection.db_config import db

validacion_bp = Blueprint('validacion_bp', __name__)

@validacion_bp.route('/validaciones', methods=['GET'])
def get_validaciones():
    dao = ValidacionRepository(db)
    validaciones = dao.get_all_validaciones()
    return jsonify([v.__dict__ for v in validaciones])

@validacion_bp.route('/validaciones/<int:id_validacion>', methods=['GET'])
def get_validacion(id_validacion):
    dao = ValidacionRepository(db)
    validacion = dao.get_validacion(id_validacion)
    return jsonify(validacion.__dict__) if validacion else (jsonify({"error": "Validación no encontrada"}), 404)

@validacion_bp.route('/validaciones', methods=['POST'])
def create_validacion():
    data = request.json
    dao = ValidacionRepository(db)
    validacion = dao.create_validacion(data['id_conciliacion'], data['id_usuario'], data['estado'], data.get('saldo_ajustado', None), data.get('comentarios', ''))
    return jsonify(validacion.__dict__), 201

@validacion_bp.route('/validaciones/<int:id_validacion>', methods=['PUT'])
def update_validacion(id_validacion):
    data = request.json
    dao = ValidacionRepository(db)
    validacion = dao.update_validacion(id_validacion, data['estado'], data.get('saldo_ajustado', None), data.get('comentarios', ''))
    return jsonify(validacion.__dict__) if validacion else (jsonify({"error": "Validación no encontrada"}), 404)

@validacion_bp.route('/validaciones/<int:id_validacion>', methods=['DELETE'])
def delete_validacion(id_validacion):
    dao = ValidacionRepository(db)
    validacion = dao.delete_validacion(id_validacion)
    return jsonify({"message": "Validación eliminada"}) if validacion else (jsonify({"error": "Validación no encontrada"}), 404)
