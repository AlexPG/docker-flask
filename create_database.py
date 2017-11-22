from run import app
from website import db
from website.shop.models import Product


with app.app_context():

    db.create_all()
