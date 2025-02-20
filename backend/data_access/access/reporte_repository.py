from data_access.models.reporte_model import Reporte

class ReporteRepository:
    def __init__(self, db_session):
        self.db = db_session

    def get_reporte(self, id_reporte: int):
        return self.db.session.query(Reporte).filter(Reporte.id_reporte == id_reporte).first()
    
    def get_all_reportes(self):
        return self.db.session.query(Reporte).all()

    def create_reporte(self, id_usuario: int, tipo_reporte: str, contenido: str):
        nuevo_reporte = Reporte(id_usuario=id_usuario, tipo_reporte=tipo_reporte, contenido=contenido)
        self.db.session.add(nuevo_reporte)
        self.db.session.commit()
        self.db.session.refresh(nuevo_reporte)
        return nuevo_reporte

    def update_reporte(self, id_reporte: int, tipo_reporte: str, contenido: str):
        reporte = self.get_reporte(id_reporte)
        if reporte:
            reporte.tipo_reporte = tipo_reporte
            reporte.contenido = contenido
            self.db.session.commit()
            self.db.session.refresh(reporte)
        return reporte

    def delete_reporte(self, id_reporte: int):
        reporte = self.get_reporte(id_reporte)
        if reporte:
            self.db.session.delete(reporte)
            self.db.session.commit()
        return reporte
