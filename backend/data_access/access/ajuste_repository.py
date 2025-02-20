from data_access.models.ajuste_model import Ajuste

class AjusteRepository:
    def __init__(self, db_session):
        self.db = db_session

    def get_ajuste(self, id_ajuste: int):
        return self.db.session.query(Ajuste).filter(Ajuste.id_ajuste == id_ajuste).first()
    
    def get_all_ajustes(self):
        return self.db.session.query(Ajuste).all()

    def create_ajuste(self, id_conciliacion: int, id_usuario: int, tipo_ajuste: str, monto: float, descripcion: str):
        nuevo_ajuste = Ajuste(id_conciliacion=id_conciliacion, id_usuario=id_usuario, tipo_ajuste=tipo_ajuste, monto=monto, descripcion=descripcion)
        self.db.session.add(nuevo_ajuste)
        self.db.session.commit()
        self.db.session.refresh(nuevo_ajuste)
        return nuevo_ajuste

    def update_ajuste(self, id_ajuste: int, tipo_ajuste: str, monto: float, descripcion: str):
        ajuste = self.get_ajuste(id_ajuste)
        if ajuste:
            ajuste.tipo_ajuste = tipo_ajuste
            ajuste.monto = monto
            ajuste.descripcion = descripcion
            self.db.session.commit()
            self.db.session.refresh(ajuste)
        return ajuste

    def delete_ajuste(self, id_ajuste: int):
        ajuste = self.get_ajuste(id_ajuste)
        if ajuste:
            self.db.session.delete(ajuste)
            self.db.session.commit()
        return ajuste