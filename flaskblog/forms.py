from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField, FloatField, validators, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User
from flask_login import current_user


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



class ProjectForm(FlaskForm):  
    username = StringField('You are (first & last name):', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email :', validators=[DataRequired(), Email()])
    ##
    project_title = StringField('Project title :', validators=[DataRequired(), Length(min=2, max=20)])
    organism = StringField('Organism (funding succeptible) :', validators=[DataRequired(), Length(min=2, max=40)])
    principal_investigator = StringField('Principal investigator :', validators=[DataRequired(), Length(min=2, max=20)])
    promotor = StringField('Promotor (eg, APHP, DRCI ...) :', validators=[DataRequired(), Length(min=2, max=20)])
    ##
    urgency_of_request = SelectField('Urgency of request :', choices=[('value1', 'Not urgent'),
                                                                      ('value2', 'Not very urgent'),
                                                                      ('value3', 'Not particularly urgent'),
                                                                      ('value4', 'Rather urgent'),
                                                                      ('value5', 'Very urgent')
                                                                      ])
    if_urgency = TextAreaField('If very urgent, briefly explain the issues :', validators=[Length(min=2, max=50)])
    ##
    project_context = TextAreaField('Project context :', validators=[DataRequired()])
    project_summary = TextAreaField('Project summary :', validators=[DataRequired()])
    bioF_needs = TextAreaField('Needs for analysis and expertise in bioinformatics and biostatistics :', validators=[DataRequired()])
    data_available = BooleanField('Data is available and accessible?', validators=[DataRequired()])
    access_data = StringField('How can we access data? ', validators=[DataRequired()])
    data_owner = StringField('Data owner :', validators=[DataRequired()])
    regulatory_requirements = BooleanField('Regulatory requirements are available?')
    if_regulatory_requirements = SelectField('If yes, precise : ', choices=[('value1', 'CPP'),
                                                                            ('value2', 'Ethical Comity'),
                                                                            ('value3', 'Jarde law conformity'),
                                                                            ('value4', 'Other'),
                                                                            ])
    data_type = StringField('Data type : ', validators=[DataRequired(), Length(min=2, max=10)])
    data_size = StringField('Data size : ', validators=[DataRequired(), Length(min=2, max=10)])
    add_info = TextAreaField('Additional informations if needs : ')

    submit = SubmitField('Validate and Send')


class GrantForm(FlaskForm):  
    username = StringField('You are :', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email :', validators=[DataRequired(), Email()])
    ##
    project_title = StringField('Project title :', validators=[DataRequired(), Length(min=2, max=20)])
    organism = StringField('Organism :', validators=[DataRequired(), Length(min=2, max=40)])
    principal_investigator = StringField('Principal investigator :', validators=[DataRequired(), Length(min=2, max=20)])
    promotor = StringField('Promotor :', validators=[DataRequired(), Length(min=2, max=20)])
    ##
    funding_type = StringField('Funding type :', validators=[DataRequired(), Length(min=2, max=20)])
    total_amount = FloatField('Total amount :', validators=[validators.InputRequired(), validators.NumberRange(min=0, max=100000)])
    ##
    deadline = DateField('Deadline', format='%m/%d/%Y', validators=[validators.InputRequired()])
    urgency_of_request = SelectField('Urgency of request :', choices=[('value1', 'Not urgent'),
                                                                      ('value2', 'Not very urgent'),
                                                                      ('value3', 'Not particularly urgent'),
                                                                      ('value4', 'Rather urgent'),
                                                                      ('value5', 'Very urgent')
                                                                      ])
    if_urgency = TextAreaField('If very urgent, briefly explain the issues :', validators=[Length(min=2, max=50)])
    ##
    project_context = TextAreaField('Project context :', validators=[DataRequired()])
    project_summary = TextAreaField('Project summary :', validators=[DataRequired()])
    bioF_needs = TextAreaField('Needs for analysis and expertise in bioinformatics and biostatistics :', validators=[DataRequired()])
    data_available = BooleanField('Data is available and accessible?', validators=[DataRequired()])
    access_data = StringField('How can we access data? ', validators=[DataRequired()])
    data_owner = StringField('Data owner :', validators=[DataRequired()])
    regulatory_requirements = BooleanField('Regulatory requirements are available?')
    if_regulatory_requirements = SelectField('If yes, precise : ', choices=[('value1', 'CPP'),
                                                                            ('value2', 'Ethical Comity'),
                                                                            ('value3', 'Jarde law conformity'),
                                                                            ('value4', 'Other'),
                                                                            ])
    data_type = StringField('Data type (eg, fastq, count table, bam ...): ', validators=[DataRequired(), Length(min=2, max=10)])
    data_size = FloatField('Data size (GO) :', validators=[validators.InputRequired(), validators.NumberRange(min=0, max=1000)])
    add_info = TextAreaField('Additional informations if needs (eg, biblio): ')

    submit = SubmitField('Validate and Send')
    