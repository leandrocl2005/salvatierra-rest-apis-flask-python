from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

stores = [{
    'name': 'My Store',
    'items': [{'name':'my item', 'price': 15.99 }]
}]

@app.route("/hello") # hello world example
def hello():
    return "Hello, world!"

@app.route('/') # render template example
def home():
  return render_template('index.html')

@app.route('/store') # get /store
def get_stores():
  return jsonify({'stores': stores})

@app.route('/store/<string:name>') #get /store/<name> data: {name :}
def get_store(name):
  for store in stores:
    if store['name'] == name:
          return jsonify(store)
  return jsonify ({'message': 'store not found'})

@app.route('/store' , methods=['POST']) #post /store data: {name :}
def create_store():
  request_data = request.get_json()
  new_store = {
    'name':request_data['name'],
    'items':[]
  }
  stores.append(new_store)
  return jsonify(new_store)

@app.route('/store/<string:name>/item' , methods=['POST']) #post /store/<name>/item data: {name :}
def create_item_in_store(name):
  request_data = request.get_json()
  for store in stores:
    if store['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'store not found'})

@app.route('/store/<string:name>/item') #get /store/<name>/item data: {name :}
def get_item_in_store(name):
  for store in stores:
    if store['name'] == name:
        return jsonify( {'items':store['items'] } )
  return jsonify ({'message':'store not found'})

app.run(port=5000)