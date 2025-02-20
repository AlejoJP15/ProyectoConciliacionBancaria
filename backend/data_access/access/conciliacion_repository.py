from data_access.models.conciliacion_model import Conciliacion

class ConciliacionRepository:
    def __init__(self, db_session):
        self.db = db_session

    def get_conciliacion(self, id_conciliacion: int):
        return self.db.session.query(Conciliacion).filter(Conciliacion.id_conciliacion == id_conciliacion).first()
    
    def get_all_conciliaciones(self):
        return self.db.session.query(Conciliacion).all()

    def create_conciliacion(self, id_usuario: int, id_cuenta: int, id_transaccion: int, estado: str, observaciones: str):
        nueva_conciliacion = Conciliacion(id_usuario=id_usuario, id_cuenta=id_cuenta, id_transaccion=id_transaccion, estado=estado, observaciones=observaciones)
        self.db.session.add(nueva_conciliacion)
        self.db.session.commit()
        self.db.session.refresh(nueva_conciliacion)
        return nueva_conciliacion

    def update_conciliacion(self, id_conciliacion: int, estado: str, observaciones: str):
        conciliacion = self.get_conciliacion(id_conciliacion)
        if conciliacion:
            conciliacion.estado = estado
            conciliacion.observaciones = observaciones
            self.db.session.commit()
            self.db.session.refresh(conciliacion)
        return conciliacion

    def delete_conciliacion(self, id_conciliacion: int):
        conciliacion = self.get_conciliacion(id_conciliacion)
        if conciliacion:
            self.db.session.delete(conciliacion)
            self.db.session.commit()
        return conciliacion
