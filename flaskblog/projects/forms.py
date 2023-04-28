from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, BooleanField, FloatField, validators, DateField, RadioField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from flaskblog.models import User


class ProjectForm(FlaskForm):  
    username = StringField('You are :*', validators=[DataRequired(),Length(min=2, max=20)],
                           render_kw={'placeholder': 'first and last name'})
    email = StringField('Email :*', validators=[DataRequired(), Email()],
                        render_kw={'placeholder': 'firstName.lastName@aphp.fr'})
    ##
    project_title = StringField('Project title :*', validators=[DataRequired(), Length(min=2, max=20)],
                                render_kw={'placeholder': 'project Name'})
    
    application = SelectField('Application :*', choices=[('For diagnosis', 'For diagnosis'),
                                              ('For research', 'For research')
                                              ])
    organism = StringField('Organism (funding succeptible) :*', validators=[DataRequired(), Length(min=2, max=40)],
                           render_kw={'placeholder': 'Structure or organization funding the project'})
    
    principal_investigator = StringField('Principal investigator :*', validators=[DataRequired(), Length(min=2, max=20)],
                                         render_kw={'placeholder': 'first and last name'})
    
    promotor = StringField('Promotor :*', validators=[DataRequired(), Length(min=2, max=20)],
                           render_kw={'placeholder': 'promotor(s) names (ex: APHP, DRCI)'})
    ##
    urgency_of_request = SelectField('Urgency of request :*', choices=[('Not urgent', 'Not urgent'),
                                                                      ('Not particularly urgent', 'Not particularly urgent'),
                                                                      ('Very urgent', 'Very urgent')
                                                                      ])
    
    if_urgency = TextAreaField('If very urgent, briefly explain the issues :*', validators=[Length(min=2, max=50)],
                               render_kw={'placeholder': 'Explain the reason for the emergency, depending on what has been selected from the drop-down list'})
    ##
    project_context = TextAreaField('Project context :*', validators=[DataRequired(), Length(min=10, max=1000)],
                                    render_kw={'placeholder': 'General explanations of the context of the project (ex : explain the rationale for the project, previous experiences or publications, general explanations of the disease, etc.)'})
    project_context_private = TextAreaField('Project context private:*', validators=[DataRequired(), Length(min=10, max=1000)],
                                    render_kw={'placeholder': 'General explanations of the context of the project (ex : explain the rationale for the project, previous experiences or publications, general explanations of the disease, etc.)'})
    project_summary = TextAreaField('Project summary :*', validators=[DataRequired(), Length(min=10, max=1000)],
                                    render_kw={'placeholder': 'Summary of the project itself, objectives, etc.'})
    bioF_needs = TextAreaField('Needs for analysis and expertise in bioinformatics and biostatistics :*', validators=[DataRequired()],
                               render_kw={'placeholder': 'Techniques, tools, types of results, etc.'})
    data_available = BooleanField('Data is available and accessible?', validators=[DataRequired()],)
    access_data = StringField('if yes, precise : ', validators=[DataRequired()],
                              render_kw={'placeholder': 'How can we access data? '})
    data_owner = StringField('Data owner :', validators=[DataRequired()], 
                             render_kw={'placeholder': 'Qui detient les donnees?'})
    regulatory_requirements = BooleanField('Regulatory requirements are available?*')
    if_regulatory_requirements = SelectField('If yes, precise : ', choices=[('CPP', 'CPP'),
                                                                            ('Ethical Comity', 'Ethical Comity'),
                                                                            ('Jarde law conformity', 'Jarde law conformity'),
                                                                            ('Other', 'Other')
                                                                            ])
    data_type = StringField('Data type :*', validators=[DataRequired(), Length(min=2, max=10)],
                            render_kw={'placeholder': 'ex: fastq, tables de comptage, bam, etc.'})
    data_size = FloatField('Data size(GO) :*', validators=[validators.InputRequired(), validators.NumberRange(min=0, max=1000)],
                           render_kw={'placeholder': 'Approximate, in GO'})
    add_info = TextAreaField('Additional informations if needs :',
                             render_kw={'placeholder': 'Example: biblio, precision(s) not filled in without the previous fields, expired valuation(s) (ex: publication), etc.'})

    submit = SubmitField('Send and get your project recap')

class GrantForm(FlaskForm):
    username = StringField('You are :*', validators=[DataRequired(),Length(min=2, max=20)],render_kw={'placeholder': 'First and Last Name'})
    email = StringField('Email :*', validators=[DataRequired(), Email()],render_kw={'placeholder': 'firstName.lastName@aphp.fr'})
    project_title = StringField('Project title :*', validators=[DataRequired(), Length(min=2, max=50)],render_kw={'placeholder': 'Project Name'})
    application = SelectField('Application :*', choices=[('For diagnosis', 'For diagnosis'),('For research', 'For research')])
    organism = StringField('Organism (funding succeptible) :*', validators=[DataRequired(), Length(min=2, max=40)],render_kw={'placeholder': 'Structure or organization funding the project'})
    principal_investigator = StringField('Principal investigator :*', validators=[DataRequired(), Length(min=2, max=40)],render_kw={'placeholder': 'First and Last Name'})
    promotor = StringField('Promotor :*', validators=[DataRequired(), Length(min=2, max=40)],render_kw={'placeholder': 'Name of the promoter(s) (ex: APHP, DRCI)'})
    funding_type = StringField('Funding type :', validators=[DataRequired(), Length(min=2, max=20)])
    total_amount = FloatField('Total amount :', validators=[validators.InputRequired(), validators.NumberRange(min=0, max=100000)])
    deadline = DateField('Deadline', format='%Y-%m-%d', validators=[validators.InputRequired()], render_kw={'placeholder':'jj/mm/aaaa'})
    urgency_of_request = SelectField('Urgency of request :', choices=[('Not urgent', 'Not urgent'),
                                                                      ('Not particularly urgent', 'Not particularly urgent'),
                                                                      ('Very urgent', 'Very urgent')
                                                                      ])
    if_urgency = TextAreaField('If very urgent, briefly explain the issues :', validators=[Length(min=2, max=200)],render_kw={'placeholder': 'Explain the reason for the emergency, depending on what has been selected from the drop-down list'})
    project_context = TextAreaField('Project context :*', validators=[DataRequired(), Length(min=10)],render_kw={'placeholder': 'General explanations of the context related to the project (e.g., explain the reason for the project, previous experiences or publications, general explanations of the disease, etc.)'})
    project_context_private = TextAreaField('Project context private :*', validators=[Length(min=10)],render_kw={'placeholder': 'General explanation of the private context related to the project (e.g., explain the reason for the project, previous experiences or publications, general explanation of the disease, etc.)'})
    project_summary = TextAreaField('Project summary :*', validators=[DataRequired(), Length(min=10)],render_kw={'placeholder': 'Summary of the project itself, objectives, etc.'})
    bioF_needs = TextAreaField('Needs for analysis and expertise in bioinformatics and biostatistics :*', validators=[DataRequired()],render_kw={'placeholder': 'Techniques, tools, types of results, etc.'})
    data_available = RadioField('Data is available and accessible?*', validators=[DataRequired()],choices=[('No','No'),('Yes','Yes')])
    access_data = StringField('if yes, precise : ', validators=[DataRequired()],render_kw={'placeholder': 'How can we access data? '})
    data_owner = StringField('Data owner :', validators=[DataRequired()],render_kw={'placeholder': 'Who owns the data?'})
    regulatory_requirements = RadioField('Regulatory requirements are available?*', validators=[DataRequired()],choices=[('No','No'),('Yes','Yes')])
    if_regulatory_requirements = SelectField('If yes, precise : ', choices=[('CPP', 'CPP'),
                                                                            ('Ethical Comity', 'Ethical Comity'),
                                                                            ('Jarde law conformity', 'Jarde law conformity'),
                                                                            ('Other', 'Other')
                                                                            ])
    data_type = StringField('Data type :*', validators=[DataRequired(), Length(min=2)],render_kw={'placeholder': 'examples: fastq, count tables, bam, etc.'})
    data_size = FloatField('Data size(GO) :*', validators=[validators.InputRequired(), validators.NumberRange(min=0, max=1000)],render_kw={'placeholder': 'Approximately, in GO'})
    add_info = TextAreaField('Additional informations if needs :',render_kw={'placeholder': 'Example: biblio, precision(s) not filled in without the previous fields, expired valuation(s) (ex: publication), etc.'})

    submit = SubmitField('Send and get your project recap')    
    

# project
class RequestProjectForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request project Sending')

    def validate_email(self, email):
        user = User.query.filter_by(email= email.data).first()
        if user is None:
            raise ValidationError('There is no account with this email. You must register first!') #template of validation method