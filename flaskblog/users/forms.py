from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', # html label
                           validators=[DataRequired(), Length(min=2, max=20)]) #list of validations that we want to check
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username= username.data).first()
        if user:
            raise ValidationError('That user name is taken. Please choose another one') #template of validation method
        
    def validate_email(self, email):
        user = User.query.filter_by(email= email.data).first()
        if user:
            raise ValidationError('That user email is taken. Please choose another one') #template of validation method

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', # html label
                           validators=[DataRequired(), Length(min=2, max=20)]) #list of validations that we want to check
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username= username.data).first()
            if user:
                raise ValidationError('That user name is taken. Please choose another one') #template of validation method
        
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email= email.data).first()
            if user:
                raise ValidationError('That user email is taken. Please choose another one') #template of validation method


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me') #remember the password
    submit = SubmitField('Login')


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Passord Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email= email.data).first()
        if user is None:
            raise ValidationError('There is no account with this email. You must register first!') #template of validation method
        
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Reset Password')


### bioinformaticiens
class BioRegistrationForm(FlaskForm):
    aphp_Num = StringField('APHP_Num', # html label
                           validators=[DataRequired(), Length(min=7, max=7)],
                           render_kw={'placeholder': '1234567'}) #list of validations that we want to check
    email = StringField('Email',
                        validators=[DataRequired(), Email()],
                        render_kw={'placeholder': 'prenom.nom@aphp.fr'})
    password = PasswordField('Password', validators=[DataRequired()],
                             render_kw={'placeholder': '***************'})
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')],
                                     render_kw={'placeholder': '***************'})
    submit = SubmitField('Sign Up')

    def validate_aphp_Num(self, aphp_Num):
        user_bio = User_bio.query.filter_by(aphp_Num= aphp_Num.data).first()
        if user_bio:
            raise ValidationError('That user aphp_Num is taken. Please choose another one') #template of validation method
        
    def validate_email(self, email):
        user_bio = User_bio.query.filter_by(email= email.data).first()
        if user_bio:
            raise ValidationError('That user email is taken. Please choose another one') #template of validation method