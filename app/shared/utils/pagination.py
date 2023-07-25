from flask import request, current_app, jsonify
from functools import wraps

from flask import request

def with_pagination(model, serializer, per_page_default=25):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', per_page_default))
        order_by = request.args.get('order', None)

        if page < 1 or per_page < 1:
          return jsonify({'error': 'Os parâmetros de paginação devem ser inteiros positivos.'}), 400  # Resposta com o código HTTP 400 (Bad Request)

        query = model.query

        if order_by:
          # Verifica se o parâmetro de ordenação é válido
          if hasattr(model, order_by):
            query = query.order_by(getattr(model, order_by))
          else:
            return jsonify({'error': 'Parâmetro de ordenação inválido.'}), 400

        pagination = query.paginate(page=page, per_page=per_page)
        items = [serializer(item) for item in pagination.items]

        response_data = {
          'companies': items,
          'pagination': {
            'total': pagination.total,
            'pages': pagination.pages,
            'page': pagination.page,
            'per_page': pagination.per_page
          }
        }

        if not items:
          response_data['message'] = 'Não foram encontrados dados correspondentes à consulta.'

        return func(*args, **kwargs, response_data=response_data)
      except Exception as e:
        current_app.logger.error(f"Erro ao buscar dados: {str(e)}")
        return jsonify({'error': 'Erro ao buscar dados.'}), 500

    return wrapper
  return decorator

