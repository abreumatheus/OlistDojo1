import sys
sys.path.append('.')

from flask import Flask, render_template, request, redirect

from src.controllers.sport_controller import SportController
from src.models.sport import Sport
from src.controllers.team_controller import TeamController
from src.models.team import Team

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


@app.route('/customer')
def customer():
    return render_template('customer.html')


@app.route('/product')
def product():
    return render_template('product.html')


app.run(debug=True)
