from connection.db_config import db
from datetime import datetime

class Conciliacion(db.Model):
    __tablename__ = "conciliaciones"

    id_conciliacion = db.Column(db.Integer, primary_key=True, index=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_cuenta = db.Column(db.Integer, db.ForeignKey('cuentas_bancarias.id_cuenta'), nullable=False)
    id_transaccion = db.Column(db.Integer, db.ForeignKey('transacciones.id_transaccion'), nullable=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    estado = db.Column(db.String(50), nullable=False)  # Pendiente, Aprobada, Rechazada
    observaciones = db.Column(db.Text, nullable=True)
