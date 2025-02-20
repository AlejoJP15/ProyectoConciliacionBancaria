from data_access.models.cuenta_bancaria_model import CuentaBancaria

class CuentaBancariaRepository:
    def __init__(self, db_session):
        self.db = db_session

    def get_cuenta(self, id_cuenta: int):
        return self.db.session.query(CuentaBancaria).filter(CuentaBancaria.id_cuenta == id_cuenta).first()
    
    def get_all_cuentas(self):
        return self.db.session.query(CuentaBancaria).all()

    def create_cuenta(self, id_usuario: int, numero_cuenta: str, banco: str, tipo_cuenta: str, saldo_calculado: float):
        nueva_cuenta = CuentaBancaria(id_usuario=id_usuario, numero_cuenta=numero_cuenta, banco=banco, tipo_cuenta=tipo_cuenta, saldo_calculado=saldo_calculado)
        self.db.session.add(nueva_cuenta)
        self.db.session.commit()
        self.db.session.refresh(nueva_cuenta)
        return nueva_cuenta

    def update_cuenta(self, id_cuenta: int, numero_cuenta: str, banco: str, tipo_cuenta: str, saldo_calculado: float):
        cuenta = self.get_cuenta(id_cuenta)
        if cuenta:
            cuenta.numero_cuenta = numero_cuenta
            cuenta.banco = banco
            cuenta.tipo_cuenta = tipo_cuenta
            cuenta.saldo_calculado = saldo_calculado
            self.db.session.commit()
            self.db.session.refresh(cuenta)
        return cuenta

    def delete_cuenta(self, id_cuenta: int):
        cuenta = self.get_cuenta(id_cuenta)
        if cuenta:
            self.db.session.delete(cuenta)
            self.db.session.commit()
        return cuenta