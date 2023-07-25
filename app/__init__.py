from flask import Flask, jsonify
from .infra.db.sqlalchemy import config_db

def make_app():
  app = Flask(__name__)

  config_db(app)

  from .modules.company.blueprint import bp_companies
  app.register_blueprint(bp_companies)

  @app.errorhandler(Exception)
  def handle_global_error(error):
    app.logger.error(f"Erro não tratado: {str(error)}")
    return jsonify({'error': 'Ocorreu um erro no servido, contete  equipe de suporte.'}), 500
  
  return app
 