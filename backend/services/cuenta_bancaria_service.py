from flask import Blueprint, request, jsonify
from data_access.access.cuenta_bancaria_repository import CuentaBancariaRepository
from connection.db_config import db

cuenta_bp = Blueprint('cuenta_bp', __name__)

@cuenta_bp.route('/cuentas', methods=['GET'])
def get_cuentas():
    dao = CuentaBancariaRepository(db)
    cuentas = dao.get_all_cuentas()
    return jsonify([c.__dict__ for c in cuentas])

@cuenta_bp.route('/cuentas/<int:id_cuenta>', methods=['GET'])
def get_cuenta(id_cuenta):
    dao = CuentaBancariaRepository(db)
    cuenta = dao.get_cuenta(id_cuenta)
    return jsonify(cuenta.__dict__) if cuenta else (jsonify({"error": "Cuenta no encontrada"}), 404)

@cuenta_bp.route('/cuentas', methods=['POST'])
def create_cuenta():
    data = request.json
    dao = CuentaBancariaRepository(db)
    cuenta = dao.create_cuenta(data['id_usuario'], data['numero_cuenta'], data['banco'], data['tipo_cuenta'], data['saldo_calculado'])
    return jsonify(cuenta.__dict__), 201

@cuenta_bp.route('/cuentas/<int:id_cuenta>', methods=['PUT'])
def update_cuenta(id_cuenta):
    data = request.json
    dao = CuentaBancariaRepository(db)
    cuenta = dao.update_cuenta(id_cuenta, data['numero_cuenta'], data['banco'], data['tipo_cuenta'], data['saldo_calculado'])
    return jsonify(cuenta.__dict__) if cuenta else (jsonify({"error": "Cuenta no encontrada"}), 404)

@cuenta_bp.route('/cuentas/<int:id_cuenta>', methods=['DELETE'])
def delete_cuenta(id_cuenta):
    dao = CuentaBancariaRepository(db)
    cuenta = dao.delete_cuenta(id_cuenta)
    return jsonify({"message": "Cuenta eliminada"}) if cuenta else (jsonify({"error": "Cuenta no encontrada"}), 404)
