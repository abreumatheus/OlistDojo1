from flask import Flask
from flask_restful import Api

from src.resources.customer_resource import CustomerResource

app = Flask(__name__)
api = Api(app)

api.add_resource(CustomerResource, '/api/customer', endpoint='customers')
api.add_resource(CustomerResource, '/api/customer/<int:id>', endpoint='customer')


@app.route('/')
def index():
    return 'Bem Vindo!'


app.run(debug=True)
