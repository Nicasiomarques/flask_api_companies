from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def config_db(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/companyDB.db'
  db.init_app(app)
  Migrate(app, db)
  app.db = db
