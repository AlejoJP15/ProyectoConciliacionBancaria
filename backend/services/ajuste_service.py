from flask import Blueprint, request, jsonify
from data_access.access.ajuste_repository import AjusteRepository
from connection.db_config import db

ajuste_bp = Blueprint('ajuste_bp', __name__)

@ajuste_bp.route('/ajustes', methods=['GET'])
def get_ajustes():
    dao = AjusteRepository(db)
    ajustes = dao.get_all_ajustes()
    return jsonify([a.__dict__ for a in ajustes])

@ajuste_bp.route('/ajustes/<int:id_ajuste>', methods=['GET'])
def get_ajuste(id_ajuste):
    dao = AjusteRepository(db)
    ajuste = dao.get_ajuste(id_ajuste)
    return jsonify(ajuste.__dict__) if ajuste else (jsonify({"error": "Ajuste no encontrado"}), 404)

@ajuste_bp.route('/ajustes', methods=['POST'])
def create_ajuste():
    data = request.json
    dao = AjusteRepository(db)
    ajuste = dao.create_ajuste(data['id_conciliacion'], data['id_usuario'], data['tipo_ajuste'], data['monto'], data.get('descripcion', ''))
    return jsonify(ajuste.__dict__), 201

@ajuste_bp.route('/ajustes/<int:id_ajuste>', methods=['PUT'])
def update_ajuste(id_ajuste):
    data = request.json
    dao = AjusteRepository(db)
    ajuste = dao.update_ajuste(id_ajuste, data['tipo_ajuste'], data['monto'], data.get('descripcion', ''))
    return jsonify(ajuste.__dict__) if ajuste else (jsonify({"error": "Ajuste no encontrado"}), 404)

@ajuste_bp.route('/ajustes/<int:id_ajuste>', methods=['DELETE'])
def delete_ajuste(id_ajuste):
    dao = AjusteRepository(db)
    ajuste = dao.delete_ajuste(id_ajuste)
    return jsonify({"message": "Ajuste eliminado"}) if ajuste else (jsonify({"error": "Ajuste no encontrado"}), 404)
