import sys

sys.path.append('.')

from flask import Flask
from flask.templating import render_template
from flask.globals import request
from werkzeug.utils import redirect
from backend.controller.product_controller import ProductController
from backend.controller.category_controller import CategoryController
from backend.model.product_model import Product
from backend.model.category_model import Category


app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/list_product')
def list_prodcut():
    controller = ProductController()
    list_ = controller.read_all()
    return render_template('list_product.html', list_ = list_)

@app.route('/list_category')
def list_category():
    controller = CategoryController()
    list_ = controller.read_all()
    return render_template('list_category.html', list_ = list_)

@app.route('/create_product')
def create_product():
    return render_template('create_product.html')

@app.route('/product', methods = ['POST'])
def product():
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    p = Product(name, description, price)
    controller = ProductController()
    controller.save(p)
    return redirect('list_product')

@app.route('/create_category')
def create_category():
    return render_template('create_category.html')

@app.route('/category', methods = ['POST'])
def category():
    name = request.form.get('name')
    description = request.form.get('description')
    c = Category(name, description)
    controller = CategoryController()
    controller.save(c)
    return redirect('list_category')

app.run()
