from connection.db_config import db
from datetime import datetime

class Validacion(db.Model):
    __tablename__ = "validaciones"

    id_validacion = db.Column(db.Integer, primary_key=True, index=True)
    id_conciliacion = db.Column(db.Integer, db.ForeignKey('conciliaciones.id_conciliacion'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    fecha_validacion = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    estado = db.Column(db.String(50), nullable=False)  # Validado, En revisión, Rechazado
    saldo_ajustado = db.Column(db.Float, nullable=True)
    comentarios = db.Column(db.Text, nullable=True)
