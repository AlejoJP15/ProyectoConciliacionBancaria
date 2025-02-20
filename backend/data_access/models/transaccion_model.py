from connection.db_config import db
from datetime import datetime

class Transaccion(db.Model):
    __tablename__ = "transacciones"

    id_transaccion = db.Column(db.Integer, primary_key=True, index=True)
    id_cuenta = db.Column(db.Integer, db.ForeignKey('cuentas_bancarias.id_cuenta'), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    monto = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # Ingreso o Egreso
    descripcion = db.Column(db.Text, nullable=True)