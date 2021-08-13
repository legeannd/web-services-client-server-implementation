from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from uuid import uuid4
from flask_uuid import FlaskUUID

app = Flask(__name__)
FlaskUUID(app)

products = [
    {
        'id': uuid4(),
        'quantity': 5,
        'value': 100,
        'name': 'Fone de ouvido'
    },
    {
        'id': uuid4(),
        'quantity': 2,
        'value': 99,
        'name': 'Carregador portátil'
    }
]

# retornar todos os produtos cadastrados
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({'products': products})

# cadastrar novo produto
@app.route('/products', methods=['POST'])
def create_product():
    if not request.json or not 'quantity' in request.json and not 'value' in request.json and not 'name' in request.json:
        abort(400)
    product = {
        'id': uuid4(),
        'name': request.json['name'],
        'quantity': request.json['quantity'],
        'value': request.json['value']
    }
    products.append(product)
    return jsonify({'product': product}), 201

# buscar produto pelo id
@app.route('/products/<uuid:productId>', methods=['GET'])
def get_product_by_id(productId):
    result = [result for result in products if result['id'] == productId]
    if len(result) == 0:
        abort(404)
    return jsonify({'product': result[0]})


# apagar produto pelo id
@app.route('/products/<uuid:productId>', methods=['DELETE'])
def delete_product(productId):
    result = [result for result in products if result['id'] == productId]
    if len(result) == 0:
        abort(404)
    products.remove(result[0])
    return jsonify({'result': True})

# alterar produto pelo id
@app.route('/products/<uuid:productId>', methods=['PUT'])
def update_product(productId):
    result = [result for result in products if result['id'] == productId]
    if len(result) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    if 'value' in request.json and type(request.json['value']) is not int:
        abort(400)
    if 'quantity' in request.json and type(request.json['quantity']) is not int:
        abort(400)
    result[0]['name'] = request.json.get('name', result[0]['name'])
    result[0]['value'] = request.json.get('value', result[0]['value'])
    result[0]['quantity'] = request.json.get('quantity', result[0]['quantity'])
    return jsonify({'product': result[0]})

# retorno padrão para rotas desconhecidas
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Resource not found'}), 404)

if __name__ == "__main__":
    print("Server live in port:5000")
    app.run(host='0.0.0.0', debug=True)
