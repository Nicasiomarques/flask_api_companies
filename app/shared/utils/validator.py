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
