from flask import request, jsonify
from functools import wraps

def validate_data(data, validations):
  errors = {}
  for field, field_validations in validations.items():
    for validation_info in field_validations:
      validation_func = validation_info['func']
      message = validation_info['message']

      if not validation_func(data.get(field)):
        errors.setdefault(field, []).append(message)

  return data, errors

def validate_request_data(validations):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      _, errors = validate_data(request.json, validations)
      if errors:
        return jsonify({'errors': errors}), 400
      return func(*args, **kwargs)
    return wrapper
  return decorator

def check_required_fields(expected_attributes):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      data = request.json
      if data is None:
        return jsonify({'error': 'Dados da requisição não foram fornecidos.'}), 400

      for attr in expected_attributes:
        if attr not in data:
          return jsonify({'error': f'O atributo {attr} está faltando na requisição.'}), 400
      return func(*args, **kwargs)
    return wrapper
  return decorator

def handle_request_errors(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except Exception as e:
      return jsonify({'error': 'Formato inválido de requisição, verifique se os campos estão escritos correctamente.'}), 400
  return wrapper
