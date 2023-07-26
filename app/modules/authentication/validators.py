import re

validate_username = lambda username: re.match(r"^[a-zA-Z0-9_]{6,20}$", username) is not None
validate_password = lambda password: re.match(r"^(?=.*[a-zA-Z])(?=.*\d).{8,}$", password) is not None

userValidators = {
  'username': [{'func': validate_username, 'message': 'Username inválido. O Username devem ter entre 6 e 20 caracteres e podem conter apenas letras, números e sublinhados.'}],
  'password': [{'func': validate_password, 'message': 'Senha inválida. A senha devem no minimo 8 caracteres e conter letras e números.'}],
}
