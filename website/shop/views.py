from flask import render_template, redirect

from . import shop
from .forms import CreateProductForm
from .models import Product
from website import db


@shop.route('/', methods=['GET'])
def product_list():
    products = Product.query.all()
    return render_template('shop/product_list.html', products=products)


@shop.route('/create', methods=['GET', 'POST'])
def product_create():
    form = CreateProductForm()
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            description=form.description.data,
        )
        db.session.add(product)
        db.session.commit()
        return redirect('/')
    return render_template('shop/product_create.html', form=form)
