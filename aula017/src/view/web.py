import sys
sys.path.append('.')
from flask import Flask, render_template, request, redirect
from src.models.customer import Customer
from src.controllers.customer_controller import CustomerController


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/sport')
def sport():
    return render_template('sport.html')

@app.route('/customer')
def customer():
    controller_customer = CustomerController()
    list_customer = controller_customer.read_all()
    return render_template('customer.html', list_customer = list_customer)

@app.route('/create_customer', methods=['GET','POST'])
def create_customer():
    if request.form.get('name'):
        name = request.form.get('name')
        num_doc = request.form.get('identification')
        phone = request.form.get('phone')
        controller_customer = CustomerController()
        customer = Customer(name,num_doc,phone)
        controller_customer.create(customer)
        return redirect('/customer')
    return render_template('form_create_customer.html')
app.run(debug=True)