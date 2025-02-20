from connection.db_config import db
from datetime import datetime

class Reporte(db.Model):
    __tablename__ = "reportes"

    id_reporte = db.Column(db.Integer, primary_key=True, index=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    fecha_generacion = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    tipo_reporte = db.Column(db.String(50), nullable=False)  # Conciliación, Auditoría
    contenido = db.Column(db.Text, nullable=False)

