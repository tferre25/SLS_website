from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, BooleanField, FloatField, validators, DateField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from flaskblog.models import User


class ProjectForm(FlaskForm):  
    username = SelectField('You are* :', choices=[('Another_DMU', 'Another_DMU'),('BioGem', 'BioGem')], validators=[DataRequired()])
    application = SelectField('Application :', choices=[('For_research', 'For research (Another DMU)'),('For_diagnosis', 'For diagnosis')])
    # REQUIRED
    email = StringField('Email* :', validators=[DataRequired(), Email()],render_kw={'placeholder': 'firstName.lastName@aphp.fr'})
    project_title = StringField('Project title :*', validators=[DataRequired(), Length(min=2)],render_kw={'placeholder': 'project Name'})
    # NOT REQUIRED
    organism = StringField('Organism (funding succeptible) :',render_kw={'placeholder': 'Structure or organization funding the project'})
    principal_investigator = StringField('Principal investigator :',render_kw={'placeholder': 'first and last name'})
    promotor = StringField('Promotor :',render_kw={'placeholder': 'promotor(s) names (ex: APHP, DRCI)'})
    
    data_available = SelectField('Data is available?:*', choices=[('0', 'No'),('1', 'Yes')])
    access_data = StringField('if available, please precise : ', validators=[DataRequired()],render_kw={'placeholder': 'How can we access data? '})

    add_info = TextAreaField('Additional informations if needs :',render_kw={'placeholder': 'Example: biblio, precision(s) not filled in without the previous fields, expired valuation(s) (ex: publication), etc.'})

    # REQUIRED
    urgency_of_request = SelectField('Urgency of request :*', choices=[('nu', 'Not urgent'),
                                                                      ('npu', 'Not particularly urgent'),
                                                                      ('vu', 'Very urgent')
                                                                      ])
    if_urgency = TextAreaField('If very urgent, please briefly explain the issues :*', validators=[DataRequired(), Length(min=10)],render_kw={'placeholder': 'Explain the reason for the emergency, depending on what has been selected from the drop-down list'})
    
    project_context = TextAreaField('Project context :*', validators=[DataRequired(), Length(min=10)],render_kw={'placeholder': 'General explanations of the context of the project (ex : explain the rationale for the project, previous experiences or publications, general explanations of the disease, etc.)'})
    project_context_private = TextAreaField('Project context private:*', validators=[DataRequired(), Length(min=10)],render_kw={'placeholder': 'General explanations of the context of the project (ex : explain the rationale for the project, previous experiences or publications, general explanations of the disease, etc.)'})
    project_summary = TextAreaField('Project summary :*', validators=[DataRequired(), Length(min=10)],render_kw={'placeholder': 'Summary of the project itself, objectives, etc.'})
    bioF_needs = TextAreaField('Needs for analysis and expertise in bioinformatics and biostatistics :*', validators=[DataRequired()],render_kw={'placeholder': 'Techniques, tools, types of results, etc.'})
    
    data_owner = StringField('Data owner :', validators=[DataRequired()],render_kw={'placeholder': 'Who owns the data?'})
    
    regulatory_requirements = SelectField('Regulatory requirements are available?*:', choices=[('0', 'No'),('1', 'Yes')])
    if_regulatory_requirements = SelectField('If regulatory requirements are available, please precise : ', choices=[('CPP', 'CPP'),
                                                                                                                    ('Ethical Comity', 'Ethical Comity'),
                                                                                                                    ('Jarde law conformity', 'Jarde law conformity'),
                                                                                                                    ('Other', 'Other')
                                                                                                                    ])
    data_type = StringField('Data type :*', validators=[DataRequired(), Length(min=2)],render_kw={'placeholder': 'ex: fastq, counting tables, bam, etc.'})
    data_size = FloatField('Data size(GO) :*', validators=[validators.InputRequired(), validators.NumberRange(min=0)],render_kw={'placeholder': 'Approximate, in GO'})
    
    submit = SubmitField('Send and get your project recap')

class GrantForm(FlaskForm):  
    username = SelectField('You are* :', choices=[('Another_DMU', 'Another_DMU'),('BioGem', 'BioGem')], validators=[DataRequired()])
    application = SelectField('Application :', choices=[('For_research', 'For research (Another DMU)'),('For_diagnosis', 'For diagnosis')])
    # REQUIRED
    email = StringField('Email* :', validators=[DataRequired(), Email()],render_kw={'placeholder': 'firstName.lastName@aphp.fr'})
    project_title = StringField('Project title :*', validators=[DataRequired(), Length(min=2)],render_kw={'placeholder': 'project Name'})
    # NOT REQUIRED
    organism = StringField('Organism (funding succeptible) :',render_kw={'placeholder': 'Structure or organization funding the project'})
    principal_investigator = StringField('Principal investigator :',render_kw={'placeholder': 'first and last name'})
    promotor = StringField('Promotor :',render_kw={'placeholder': 'promotor(s) names (ex: APHP, DRCI)'})
    
    data_available = SelectField('Data is available?:*', choices=[('0', 'No'),('1', 'Yes')])
    access_data = StringField('if available, please precise : ', validators=[DataRequired()],render_kw={'placeholder': 'How can we access data? '})

    add_info = TextAreaField('Additional informations if needs :',render_kw={'placeholder': 'Example: biblio, precision(s) not filled in without the previous fields, expired valuation(s) (ex: publication), etc.'})

    # REQUIRED
    urgency_of_request = SelectField('Urgency of request :*', choices=[('nu', 'Not urgent'),
                                                                      ('npu', 'Not particularly urgent'),
                                                                      ('vu', 'Very urgent')
                                                                      ])
    if_urgency = TextAreaField('If very urgent, please briefly explain the issues :*', validators=[DataRequired(), Length(min=10)],render_kw={'placeholder': 'Explain the reason for the emergency, depending on what has been selected from the drop-down list'})
    
    project_context = TextAreaField('Project context :*', validators=[DataRequired(), Length(min=10)],render_kw={'placeholder': 'General explanations of the context of the project (ex : explain the rationale for the project, previous experiences or publications, general explanations of the disease, etc.)'})
    project_context_private = TextAreaField('Project context private:*', validators=[DataRequired(), Length(min=10)],render_kw={'placeholder': 'General explanations of the context of the project (ex : explain the rationale for the project, previous experiences or publications, general explanations of the disease, etc.)'})
    project_summary = TextAreaField('Project summary :*', validators=[DataRequired(), Length(min=10)],render_kw={'placeholder': 'Summary of the project itself, objectives, etc.'})
    bioF_needs = TextAreaField('Needs for analysis and expertise in bioinformatics and biostatistics :*', validators=[DataRequired()],render_kw={'placeholder': 'Techniques, tools, types of results, etc.'})
    
    funding_type = StringField('Funding type : *', render_kw={'placeholder': 'funding type ...'})
    total_amount = FloatField('Total amount: *', render_kw={'placeholder': 'Total amount ...'})
    deadline = DateField('Deadline:')

    data_owner = StringField('Data owner :', validators=[DataRequired()],render_kw={'placeholder': 'Who owns the data?'})
    
    regulatory_requirements = SelectField('Regulatory requirements are available?*:', choices=[('0', 'No'),('1', 'Yes')])
    if_regulatory_requirements = SelectField('If regulatory requirements are available, please precise : ', choices=[('CPP', 'CPP'),
                                                                                                                    ('Ethical Comity', 'Ethical Comity'),
                                                                                                                    ('Jarde law conformity', 'Jarde law conformity'),
                                                                                                                    ('Other', 'Other')
                                                                                                                    ])
    data_type = StringField('Data type :*', validators=[DataRequired(), Length(min=2)],render_kw={'placeholder': 'ex: fastq, counting tables, bam, etc.'})
    data_size = FloatField('Data size(GO) :*', validators=[validators.InputRequired(), validators.NumberRange(min=0)],render_kw={'placeholder': 'Approximate, in GO'})
    
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