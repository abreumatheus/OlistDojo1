from flask import Flask, render_template, request, redirect

from src.controllers.sport_controller import SportController
from src.models.sport import Sport

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/team')
def team():
    return render_template('team.html')


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


@app.route('/customer')
def customer():
    return render_template('customer.html')


@app.route('/product')
def product():
    return render_template('product.html')


app.run(debug=True)
