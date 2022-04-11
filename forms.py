from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField
from wtforms.validators import Email, DataRequired, EqualTo, NumberRange


class RegistrationForm(FlaskForm):
    email = StringField('E-mail')
    password = PasswordField('Password')
    check_password = PasswordField('Repeat password ')
    surname = StringField('Name')
    age = StringField('Age')
    position = StringField('Position')
    speciality = StringField('Speciality')
    address = StringField('Address')
