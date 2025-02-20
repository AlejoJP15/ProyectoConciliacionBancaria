from flask import Blueprint, request, jsonify
from data_access.access.reporte_repository import ReporteRepository
from connection.db_config import db

reporte_bp = Blueprint('reporte_bp', __name__)

@reporte_bp.route('/reportes', methods=['GET'])
def get_reportes():
    dao = ReporteRepository(db)
    reportes = dao.get_all_reportes()
    return jsonify([r.__dict__ for r in reportes])

@reporte_bp.route('/reportes/<int:id_reporte>', methods=['GET'])
def get_reporte(id_reporte):
    dao = ReporteRepository(db)
    reporte = dao.get_reporte(id_reporte)
    return jsonify(reporte.__dict__) if reporte else (jsonify({"error": "Reporte no encontrado"}), 404)

@reporte_bp.route('/reportes', methods=['POST'])
def create_reporte():
    data = request.json
    dao = ReporteRepository(db)
    reporte = dao.create_reporte(data['id_usuario'], data['tipo_reporte'], data['contenido'])
    return jsonify(reporte.__dict__), 201

@reporte_bp.route('/reportes/<int:id_reporte>', methods=['PUT'])
def update_reporte(id_reporte):
    data = request.json
    dao = ReporteRepository(db)
    reporte = dao.update_reporte(id_reporte, data['tipo_reporte'], data['contenido'])
    return jsonify(reporte.__dict__) if reporte else (jsonify({"error": "Reporte no encontrado"}), 404)

@reporte_bp.route('/reportes/<int:id_reporte>', methods=['DELETE'])
def delete_reporte(id_reporte):
    dao = ReporteRepository(db)
    reporte = dao.delete_reporte(id_reporte)
    return jsonify({"message": "Reporte eliminado"}) if reporte else (jsonify({"error": "Reporte no encontrado"}), 404)
