from flask import render_template

from . import shop
from .models import Product


@shop.route('/')
def product_list():
    products = Product.query.all()
    return render_template('shop/product_list.html', products=products)
