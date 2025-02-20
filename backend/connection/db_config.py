from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:966921@localhost:5432/conciliacion_bancaria'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/conciliacion_bancaria'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)