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

@app.route('/product/update/', methods=['POST'])
def update_product_post():
    controller = ProductController()
    id_ = request.form.get('id_')
    product = controller.read_by_id(int(id_))
    product.name = request.form.get('name')
    product.description = request.form.get('description')
    product.price = float(request.form.get('price'))
    controller.update(product)
    return redirect('/product')      


@app.route('/product/update/<int:id>', methods=['GET'])
def update_product_get(id):
    product = ProductController().read_by_id(int(id))
    return render_template('product_create.html', product=product, action = 'Update')


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
    return render_template('product_create.html', action = 'Create')


@app.route('/product/delete/<int:id>')
def delete_product(id):
    product = ProductController().read_by_id(id)
    ProductController().delete(product)
    return redirect('/product')


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
