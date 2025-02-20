from connection.db_config import db
class CuentaBancaria(db.Model):
    __tablename__ = "cuentas_bancarias"

    id_cuenta = db.Column(db.Integer, primary_key=True, index=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    numero_cuenta = db.Column(db.String(50), unique=True, nullable=False)
    banco = db.Column(db.String(100), nullable=False)
    tipo_cuenta = db.Column(db.String(50), nullable=False)
    saldo_calculado = db.Column(db.Float, nullable=False)