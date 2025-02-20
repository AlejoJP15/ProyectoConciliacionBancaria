from data_access.models.transaccion_model import Transaccion

class TransaccionRepository:
    def __init__(self, db_session):
        self.db = db_session

    def get_transaccion(self, id_transaccion: int):
        return self.db.session.query(Transaccion).filter(Transaccion.id_transaccion == id_transaccion).first()
    
    def get_all_transacciones(self):
        return self.db.session.query(Transaccion).all()

    def create_transaccion(self, id_cuenta: int, monto: float, tipo: str, descripcion: str):
        nueva_transaccion = Transaccion(id_cuenta=id_cuenta, monto=monto, tipo=tipo, descripcion=descripcion)
        self.db.session.add(nueva_transaccion)
        self.db.session.commit()
        self.db.session.refresh(nueva_transaccion)
        return nueva_transaccion

    def update_transaccion(self, id_transaccion: int, monto: float, tipo: str, descripcion: str):
        transaccion = self.get_transaccion(id_transaccion)
        if transaccion:
            transaccion.monto = monto
            transaccion.tipo = tipo
            transaccion.descripcion = descripcion
            self.db.session.commit()
            self.db.session.refresh(transaccion)
        return transaccion

    def delete_transaccion(self, id_transaccion: int):
        transaccion = self.get_transaccion(id_transaccion)
        if transaccion:
            self.db.session.delete(transaccion)
            self.db.session.commit()
        return transaccion