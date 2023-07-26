from flask import Blueprint, current_app, jsonify, request
from flask_jwt_extended import  create_access_token, create_refresh_token
from passlib.hash import pbkdf2_sha256
from ...consts.enviroment import jwt_expires_day
from datetime import timedelta

from ...shared.utils.validator import validate_request_data, check_required_fields
from ..authentication.validators import userValidators
from ...shared.utils.parser import model_to_dict
from ..authentication.model import User

bp_authentication = Blueprint('auth', __name__)

@bp_authentication.route('/auth/signup', methods=['POST'])
@check_required_fields(['password', 'username'])
@validate_request_data(userValidators)
def signup():
  data = request.get_json()
  username, password = data['username'].lower(), pbkdf2_sha256.hash(data['password'])

  user_exists = User.query.filter_by(username=username).first()

  if user_exists:
    return jsonify({'message': 'Já existe um usuário com esse nome de usuário.'}), 400

  new_user = User(username=username, password=password)

  current_app.db.session.add(new_user)
  current_app.db.session.commit()

  return jsonify(model_to_dict(new_user)), 201

@bp_authentication.route('/auth/login', methods=['POST'])
@check_required_fields(['password', 'username'])
@validate_request_data(userValidators)
def login():
  username = request.json['username']
  password = request.json['password']

  user = User.query.filter_by(username=username).first()

  if not user or not pbkdf2_sha256.verify(password, user.password):
    return jsonify({'error': 'username ou password incorrectos!'}), 401
  print(jwt_expires_day)
  access_token = create_access_token(identity=user.id, expires_delta=timedelta(days=int(jwt_expires_day)))
  refresh_token = create_refresh_token(identity=user.id)

  return jsonify(({
    **model_to_dict(user),
    'access_token': access_token,
    'refresh_token': refresh_token
  })), 200
