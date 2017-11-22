from flask import render_template

from . import shop


@shop.route('/')
def hello():
    return render_template('shop/product_list.html')
