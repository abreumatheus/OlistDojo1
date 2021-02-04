import sys
sys.path.append('.')

from flask import Flask, render_template, request, redirect

from src.controllers.sport_controller import SportController
from src.controllers.product_controller import ProductController
from src.controllers.customer_controller import CustomerController
from src.controllers.team_controller import TeamController

from src.models.sport import Sport
from src.models.team import Team
from src.models.product import Product
from src.models.customer import Customer

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/team')
def team():
    team_list = TeamController().read_all()
    return render_template('team.html', teams=team_list)

@app.route('/team/create')
def team_create_form():
    return render_template('team_create.html')

@app.route('/team', methods=['POST'])
def team_create():
    controller = TeamController()
    name = request.form.get('name')
    description = request.form.get('description')
    new_team = Team(name, description)
    controller.create(new_team)
    return redirect('/team')

@app.route('/sport')
def sport():
    controller = SportController()
    sports_list = controller.read_all()
    return render_template('sport.html', sports=sports_list)


@app.route('/sport/create')
def sport_create_form():
    return render_template('sport_create.html')


@app.route('/sport', methods=['POST'])
def sport_create():
    controller = SportController()
    name = request.form.get('name')
    description = request.form.get('description')
    new_sport = Sport(name, description)
    controller.create(new_sport)
    return redirect('/sport')


@app.route('/product')
def product():
    controller = ProductController()
    product_list = controller.read_all()
    return render_template('product.html', products=product_list)


@app.route('/product/create', methods=['POST', 'GET'])
def create_product():
    if request.method == 'POST':
        controller = ProductController()
        name = request.form.get('name')
        description = request.form.get('description')
        price = float(request.form.get('price'))
        new_product = Product(name, price, description)
        controller.create(new_product)
        return redirect('/product')       
    return render_template('product_create.html')

@app.route('/customer')
def customer():
    controller_customer = CustomerController()
    list_customer = controller_customer.read_all()
    return render_template('customer.html', list_customer = list_customer)

@app.route('/create_customer/<action>', methods=['GET','POST'])
def create_customer(action):
    if request.form.get('name'):
        name = request.form.get('name')
        num_doc = request.form.get('identification')
        phone = request.form.get('phone')
        controller_customer = CustomerController()
        customer = Customer(name,num_doc,phone)
        controller_customer.create(customer)
        return redirect('/customer')
    return render_template('form_create_customer.html')

@app.route('/delete_customer/<int:id_>')
def delete_customer(id_):
    controller_customer = CustomerController()
    customer = controller_customer.read_by_id(id_)
    controller_customer.delete(customer)
    return redirect('/customer')

@app.route('/update_customer/<int:id_>', methods=['GET', 'POST'])
def update_customer(id_):
    controller_customer = CustomerController()
    customer = controller_customer.read_by_id(id_)
    if request.method == 'POST':
        name = request.form.get('name')
        num_doc = request.form.get('identification')
        phone = request.form.get('phone')
        customer.name = name
        customer.num_doc = num_doc
        customer.phone = phone
        controller_customer.update(customer)
        return redirect('/customer')
    return render_template('form_update_customer.html', customer = customer)

app.run(debug=True)
