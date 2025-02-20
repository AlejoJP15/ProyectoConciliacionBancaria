import sys
import os
from flask import Flask
from flask_cors import CORS
from connection.db_config import init_db
from services.usuario_service import usuario_bp
from services.cuenta_bancaria_service import cuenta_bp
from services.transaccion_service import transaccion_bp
from services.conciliacion_service import conciliacion_bp
from services.reporte_service import reporte_bp
from services.validacion_service import validacion_bp
from services.ajuste_service import ajuste_bp
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
app = Flask(__name__)
# Inicializar la aplicación Flask
app = Flask(__name__)
CORS(app)  # Permitir peticiones CORS

# Configurar la base de datos
init_db(app)

# Registrar los Blueprints de los servicios
app.register_blueprint(usuario_bp, url_prefix='/api')
app.register_blueprint(cuenta_bp, url_prefix='/api')
app.register_blueprint(transaccion_bp, url_prefix='/api')
app.register_blueprint(conciliacion_bp, url_prefix='/api')
app.register_blueprint(reporte_bp, url_prefix='/api')
app.register_blueprint(validacion_bp, url_prefix='/api')
app.register_blueprint(ajuste_bp, url_prefix='/api')


@app.route('/')
def hello():
    return "¡Conexión a la base de datos configurada correctamente!"
if __name__ == '__main__':
    app.run(debug=True)