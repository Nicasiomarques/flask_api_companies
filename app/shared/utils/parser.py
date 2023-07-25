def make_model_instance(model, data, required_fields =[]):
  for field in required_fields:
    if field not in data:
      raise ValueError(f"Campo '{field}' é obrigatório.")
  new_model_instance = model(**data)
  return new_model_instance

def model_to_dict(model_instance):
  model_dict = {}
  for column in model_instance.__table__.columns:
    column_name = column.name
    column_value = getattr(model_instance, column_name)
    model_dict[column_name] = column_value
  return model_dict

def model_instance_and_dict(model, data, required_fields =[]):
  model_instance = make_model_instance(model, data, required_fields)
  dictionary = model_to_dict(model_instance)
  return model_instance, dictionary
