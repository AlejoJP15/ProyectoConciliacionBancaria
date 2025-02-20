from flask import Blueprint, request, jsonify
from data_access.access.conciliacion_repository import ConciliacionRepository
from connection.db_config import db

conciliacion_bp = Blueprint('conciliacion_bp', __name__)

@conciliacion_bp.route('/conciliaciones', methods=['GET'])
def get_conciliaciones():
    dao = ConciliacionRepository(db)
    conciliaciones = dao.get_all_conciliaciones()
    return jsonify([c.__dict__ for c in conciliaciones])

@conciliacion_bp.route('/conciliaciones/<int:id_conciliacion>', methods=['GET'])
def get_conciliacion(id_conciliacion):
    dao = ConciliacionRepository(db)
    conciliacion = dao.get_conciliacion(id_conciliacion)
    return jsonify(conciliacion.__dict__) if conciliacion else (jsonify({"error": "Conciliación no encontrada"}), 404)

@conciliacion_bp.route('/conciliaciones', methods=['POST'])
def create_conciliacion():
    data = request.json
    dao = ConciliacionRepository(db)
    conciliacion = dao.create_conciliacion(data['id_usuario'], data['id_cuenta'], data.get('id_transaccion', None), data['estado'], data.get('observaciones', ''))
    return jsonify(conciliacion.__dict__), 201

@conciliacion_bp.route('/conciliaciones/<int:id_conciliacion>', methods=['PUT'])
def update_conciliacion(id_conciliacion):
    data = request.json
    dao = ConciliacionRepository(db)
    conciliacion = dao.update_conciliacion(id_conciliacion, data['estado'], data.get('observaciones', ''))
    return jsonify(conciliacion.__dict__) if conciliacion else (jsonify({"error": "Conciliación no encontrada"}), 404)

@conciliacion_bp.route('/conciliaciones/<int:id_conciliacion>', methods=['DELETE'])
def delete_conciliacion(id_conciliacion):
    dao = ConciliacionRepository(db)
    conciliacion = dao.delete_conciliacion(id_conciliacion)
    return jsonify({"message": "Conciliación eliminada"}) if conciliacion else (jsonify({"error": "Conciliación no encontrada"}), 404)
