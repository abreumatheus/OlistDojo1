from flask import Flask, render_template


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
    return render_template('customer.html')


@app.route('/product')
def product():
    return render_template('product.html')


app.run(debug=True)