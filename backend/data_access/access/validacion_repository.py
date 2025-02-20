from data_access.models.validacion_model import Validacion

class ValidacionRepository:
    def __init__(self, db_session):
        self.db = db_session

    def get_validacion(self, id_validacion: int):
        return self.db.session.query(Validacion).filter(Validacion.id_validacion == id_validacion).first()
    
    def get_all_validaciones(self):
        return self.db.session.query(Validacion).all()

    def create_validacion(self, id_conciliacion: int, id_usuario: int, estado: str, saldo_ajustado: float, comentarios: str):
        nueva_validacion = Validacion(id_conciliacion=id_conciliacion, id_usuario=id_usuario, estado=estado, saldo_ajustado=saldo_ajustado, comentarios=comentarios)
        self.db.session.add(nueva_validacion)
        self.db.session.commit()
        self.db.session.refresh(nueva_validacion)
        return nueva_validacion

    def update_validacion(self, id_validacion: int, estado: str, saldo_ajustado: float, comentarios: str):
        validacion = self.get_validacion(id_validacion)
        if validacion:
            validacion.estado = estado
            validacion.saldo_ajustado = saldo_ajustado
            validacion.comentarios = comentarios
            self.db.session.commit()
            self.db.session.refresh(validacion)
        return validacion

    def delete_validacion(self, id_validacion: int):
        validacion = self.get_validacion(id_validacion)
        if validacion:
            self.db.session.delete(validacion)
            self.db.session.commit()
        return validacion