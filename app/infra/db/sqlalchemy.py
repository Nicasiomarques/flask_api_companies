from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from ...consts.enviroment import database_path

db = SQLAlchemy()

def config_db(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = database_path
  db.init_app(app)
  Migrate(app, db)
  app.db = db

from ...modules.authentication.model import User
from ...modules.company.model import Company
