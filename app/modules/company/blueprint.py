from flask import Blueprint, current_app, jsonify, request

from ...shared.utils.parser import model_instance_and_dict, model_to_dict
from ...shared.utils import pagination, validator
from .validators import companyValidators
from .model import Company

bp_companies = Blueprint('companies', __name__)

@bp_companies.route('/companies', methods=['GET'])
@pagination.with_pagination(Company, model_to_dict)
def get_all(*_, **kwargs):
  response_data = kwargs['response_data']
  return jsonify(response_data), 200

@bp_companies.route('/companies', methods=['POST'])
@validator.validate_request_data(companyValidators)
def add_company():
  new_company, result = model_instance_and_dict(Company, request.json)
  company = Company.query.filter_by(cnpj=request.json['cnpj']).first()
  if company:
    return jsonify({'error': 'Ja existe uma empresa com esse CNPJ.'}), 400

  current_app.db.session.add(new_company)
  current_app.db.session.commit()
  return jsonify(result), 201

@bp_companies.route('/companies/<int:id>', methods=['GET'])
def get_company(id):
  company = Company.query.get(id)
  if not company:
    return jsonify({'error': 'Empresa não encontrada.'}), 404

  return jsonify(model_to_dict(company)), 200

@bp_companies.route('/companies/<int:id>', methods=['PUT'])
def edit_company(id):
  company = Company.query.get(id)
  if not company:
    return jsonify({'error': 'Empresa não encontrada.'}), 404

  allowed_fields = ['cnae', 'fantasyName']

  @validator.validate_request_data(companyValidators)
  def update_company():
    for key, value in request.json.items():
      if key in allowed_fields:
        setattr(company, key, value)

  update_company()
  
  current_app.db.session.commit()
  return jsonify(model_to_dict(company)), 200

@bp_companies.route('/companies/<string:cnpj>', methods=['DELETE'])
def delete_company(cnpj):
  company = Company.query.filter_by(cnpj=cnpj).first()
  if not company:
    return jsonify({'error': 'Empresa não encontrada.'}), 404
  
  current_app.db.session.delete(company)
  current_app.db.session.commit()
  return jsonify({'message': 'Empresa excluída com sucesso.'}), 200
