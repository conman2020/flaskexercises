"""Forms for our demo Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, Email


class AddSnackForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Snack Name")
    price = FloatField("Price in USD")
    quantity = FloatField("Amount in Snack")
    is_healthy = BooleanField("This is a healthy snack")
    # category = RadioField("Category", choices= [('ic','Ice Cream'), ('chips', 'Potato Chips'), ('candy', 'Candy/Sweets')])
    category = SelectField("Category", choices= [('ic','Ice Cream'), ('chips', 'Potato Chips'), ('candy', 'Candy/Sweets')])

class UserForm(FlaskForm):
    """Form for adding/editing friend."""

    name = StringField("Name",
                       validators=[InputRequired()])
    email = StringField("Email Address",
                        validators=[Optional(), Email()])

class NewEmployeeForm(FlaskForm):
    name= StringField("Employee name")
    state= StringField("Employee state")
    # dept_code= StringField("Department code")
    dept_code= SelectField("Department code")