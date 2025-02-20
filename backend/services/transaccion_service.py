from flask import Blueprint, request, jsonify
from data_access.access.transaccion_repository import TransaccionRepository
from connection.db_config import db

transaccion_bp = Blueprint('transaccion_bp', __name__)

@transaccion_bp.route('/transacciones', methods=['GET'])
def get_transacciones():
    dao = TransaccionRepository(db)
    transacciones = dao.get_all_transacciones()
    return jsonify([t.__dict__ for t in transacciones])

@transaccion_bp.route('/transacciones/<int:id_transaccion>', methods=['GET'])
def get_transaccion(id_transaccion):
    dao = TransaccionRepository(db)
    transaccion = dao.get_transaccion(id_transaccion)
    return jsonify(transaccion.__dict__) if transaccion else (jsonify({"error": "Transacción no encontrada"}), 404)

@transaccion_bp.route('/transacciones', methods=['POST'])
def create_transaccion():
    data = request.json
    dao = TransaccionRepository(db)
    transaccion = dao.create_transaccion(data['id_cuenta'], data['monto'], data['tipo'], data.get('descripcion', ''))
    return jsonify(transaccion.__dict__), 201

@transaccion_bp.route('/transacciones/<int:id_transaccion>', methods=['PUT'])
def update_transaccion(id_transaccion):
    data = request.json
    dao = TransaccionRepository(db)
    transaccion = dao.update_transaccion(id_transaccion, data['monto'], data['tipo'], data.get('descripcion', ''))
    return jsonify(transaccion.__dict__) if transaccion else (jsonify({"error": "Transacción no encontrada"}), 404)

@transaccion_bp.route('/transacciones/<int:id_transaccion>', methods=['DELETE'])
def delete_transaccion(id_transaccion):
    dao = TransaccionRepository(db)
    transaccion = dao.delete_transaccion(id_transaccion)
    return jsonify({"message": "Transacción eliminada"}) if transaccion else (jsonify({"error": "Transacción no encontrada"}), 404)
