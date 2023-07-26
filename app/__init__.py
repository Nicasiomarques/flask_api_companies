from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

from .infra.db.sqlalchemy import config_db
from .consts.enviroment import jwt_secret_key

load_dotenv()

def make_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = jwt_secret_key

  config_db(app)
  JWTManager(app)

  from .modules.company.blueprint import bp_companies
  app.register_blueprint(bp_companies)

  from .modules.authentication.blueprint import bp_authentication
  app.register_blueprint(bp_authentication)

  @app.errorhandler(Exception)
  def handle_global_error(error):
    app.logger.error(f"Erro não tratado: {str(error)}")
    return jsonify({'error': 'Ocorreu um erro no servido, contete  equipe de suporte.'}), 500
  
  return app
 