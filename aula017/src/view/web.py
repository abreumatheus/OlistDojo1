import sys

from sqlalchemy.sql.expression import true, update
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
    id_aux = request.args.get('id')
    if id_aux:
        controller = SportController()        
        sport = controller.read_by_id(int(id_aux))
        return render_template('sport_create.html', update=True, sport=sport)

    return render_template('sport_create.html')


@app.route('/sport', methods=['POST'])
def sport_create():
    controller = SportController()
    name = request.form.get('name')
    description = request.form.get('description')
    new_sport = Sport(name, description)
    controller.create(new_sport)
    return redirect('/sport')


@app.route('/sport/update', methods=['POST'])
def sport_update():
    controller = SportController()
    id_aux = int(request.form.get('id'))
    name = request.form.get('name')
    description = request.form.get('description')
    sport = controller.read_by_id(id_aux)
    sport.name = name
    sport.description = description
    controller.update(sport)
    return redirect('/sport')

@app.route('/sport/delete')
def sport_delete():
    controller = SportController()
    id_aux = int(request.args.get('id'))
    sport = controller.read_by_id(id_aux)
    controller.delete(sport)
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
