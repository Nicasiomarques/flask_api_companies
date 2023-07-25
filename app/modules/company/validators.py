import re

def validate_cnae(cnae):
  return bool(re.match(r'^[0-9]{5}-[0-9]{1}$', cnae))

isValidStr = lambda value: isinstance(value, str) and value.strip()

companyValidators = {
  'cnpj': [{'func': isValidStr, 'message': 'CNPJ inválido.'}],
  'cnae': [{'func': validate_cnae, 'message': 'CNAE inválido.'}],
  'reasonName': [{'func': isValidStr, 'message': 'Nome razão inválido.'}],
  'fantasyName': [{'func': isValidStr, 'message': 'Nome fantasia inválido.'}],
}
