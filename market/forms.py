from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists!')

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('This email already exists!')

    username = StringField('Username:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField('Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField('Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField('Repeat password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField('Create Account')


class LoginForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Sign in")


class PurchaseItemForm(FlaskForm):
    submit = SubmitField('Confirm')


class SellItemForm(FlaskForm):
    submit = SubmitField('Sell')
