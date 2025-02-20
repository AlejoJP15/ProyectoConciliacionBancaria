from connection.db_config import db

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id_usuario = db.Column(db.Integer, primary_key=True, index=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=True)  # Opcional para autenticación por correo
    contrasena_hash = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.email if self.email else self.id_usuario}>'