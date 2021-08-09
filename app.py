from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My New Store',
        'items': [
            {
                'name': 'myItem',
                'price': 16.99
            }
        ]
    }
]

# POST /store data: {name:}
@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string: name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores: #iterate over the stores
        if store['name'] == name: # if the store name matches, return it
            return jsonify(store)
    return jsonify({'message': 'Store not found'}) # if none match, return an error message

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
app.route('/store/<string:name>', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'items': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store not found'})

# GET /store/<string:name>/item
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'item not found'})

app.run(port=5000)
