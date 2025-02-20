from data_access.models.usuario_model import Usuario

class UsuarioRepository:
    def __init__(self, db_session):
        self.db = db_session

    def get_usuario(self, usuario_id: int):
        return self.db.session.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    
    def get_usuario_por_email(self, email: str):
        return self.db.session.query(Usuario).filter(Usuario.email == email).first()

    def get_all_usuarios(self):
        return self.db.session.query(Usuario).all()

    def create_usuario(self, nombre: str, email: str, contrasena_hash: str, rol: str):
        nuevo_usuario = Usuario(nombre=nombre, email=email, contrasena_hash=contrasena_hash, rol=rol)
        self.db.session.add(nuevo_usuario)
        self.db.session.commit()
        self.db.session.refresh(nuevo_usuario)
        return nuevo_usuario

    def update_usuario(self, usuario_id: int, nombre: str, email: str, contrasena_hash: str, rol: str):
        usuario = self.get_usuario(usuario_id)
        if usuario:
            usuario.nombre = nombre
            usuario.email = email
            usuario.contrasena_hash = contrasena_hash
            usuario.rol = rol
            self.db.session.commit()
            self.db.session.refresh(usuario)
        return usuario

    def delete_usuario(self, usuario_id: int):
        usuario = self.get_usuario(usuario_id)
        if usuario:
            self.db.session.delete(usuario)
            self.db.session.commit()
        return usuario