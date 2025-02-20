from connection.db_config import db
from datetime import datetime

class Ajuste(db.Model):
    __tablename__ = "ajustes"

    id_ajuste = db.Column(db.Integer, primary_key=True, index=True)
    id_conciliacion = db.Column(db.Integer, db.ForeignKey('conciliaciones.id_conciliacion'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    tipo_ajuste = db.Column(db.String(50), nullable=False)  # Añadir, Modificar, Eliminar
    monto = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.Text, nullable=True)