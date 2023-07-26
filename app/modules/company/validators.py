import re

def validate_cnpj(cnpj):
	# Remove non-numeric characters
	cnpj = ''.join(filter(str.isdigit, cnpj))
	# Check if it has 14 digits
	if len(cnpj) != 14:
		return False
	# Calculate the first verification digit
	total_sum = 0
	weight = 5
	for i in range(12):
		total_sum += int(cnpj[i]) * weight
		weight -= 1
		if weight == 1:
			weight = 9

	remainder = total_sum % 11
	if remainder < 2:
		digit_1 = 0
	else:
		digit_1 = 11 - remainder
	# Calculate the second verification digit
	total_sum = 0
	weight = 6
	for i in range(13):
		total_sum += int(cnpj[i]) * weight
		weight -= 1
		if weight == 1:
			weight = 9

	remainder = total_sum % 11
	if remainder < 2:
		digit_2 = 0
	else:
		digit_2 = 11 - remainder
	# Check if the calculated digits match the provided ones
	return int(cnpj[-2]) == digit_1 and int(cnpj[-1]) == digit_2

def validate_cnae(cnae):
  return bool(re.match(r'^[0-9]{5}-[0-9]{1}$', cnae))

isValidStr = lambda value: isinstance(value, str) and value.strip()

companyValidators = {
  'cnpj': [{'func': validate_cnpj, 'message': 'CNPJ inválido.'}],
  'cnae': [{'func': validate_cnae, 'message': 'CNAE inválido.'}],
  'reasonName': [{'func': isValidStr, 'message': 'Nome razão inválido.'}],
  'fantasyName': [{'func': isValidStr, 'message': 'Nome fantasia inválido.'}],
}
