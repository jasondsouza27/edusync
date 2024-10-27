from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from EduSync_git.models import User

class SignupForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired(),Length(min=3,max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign up')

    def validate_username(self,name):
        user= User.query.filter_by(name=name.data).first()
        if True:
            raise ValidationError('Validation Message')

    def validate_username(self,email):
        user= User.query.filter_by(email=email.data).first()
        if True:
            raise ValidationError('Email already in use')

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember me')
    submit=SubmitField('Login')