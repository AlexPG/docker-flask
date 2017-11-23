from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, optional, length


class CreateProductForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()],
                       description='Product name')
    description = TextAreaField('description', validators=[
        optional(), length(max=200)], description='Product description')
