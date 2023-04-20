from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, BooleanField, FloatField, validators, DateField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from flaskblog.models import User


class ProjectForm(FlaskForm):  
    username = StringField('You are :*', validators=[DataRequired(),Length(min=2, max=20)],
                           render_kw={'placeholder': 'Prenom et Nom'})
    email = StringField('Email :*', validators=[DataRequired(), Email()],
                        render_kw={'placeholder': 'prenom.nom@aphp.fr'})
    ##
    project_title = StringField('Project title :*', validators=[DataRequired(), Length(min=2, max=20)],
                                render_kw={'placeholder': 'Nom du projet'})
    
    application = SelectField('Application :*', choices=[('For diagnosis', 'For diagnosis'),
                                              ('For research', 'For research')
                                              ])
    organism = StringField('Organism (funding succeptible) :*', validators=[DataRequired(), Length(min=2, max=40)],
                           render_kw={'placeholder': 'Structure ouorganisme financant le projet'})
    
    principal_investigator = StringField('Principal investigator :*', validators=[DataRequired(), Length(min=2, max=20)],
                                         render_kw={'placeholder': 'Prenom et Nom'})
    
    promotor = StringField('Promotor :*', validators=[DataRequired(), Length(min=2, max=20)],
                           render_kw={'placeholder': 'Nom du ou des promoteur(s) (ex: APHP, DRCI)'})
    ##
    urgency_of_request = SelectField('Urgency of request :*', choices=[('Not urgent', 'Not urgent'),
                                                                      ('Not particularly urgent', 'Not particularly urgent'),
                                                                      ('Very urgent', 'Very urgent')
                                                                      ])
    
    if_urgency = TextAreaField('If very urgent, briefly explain the issues :*', validators=[Length(min=2, max=50)],
                               render_kw={'placeholder': 'Expliquer la raison de l\'urgence, selon ce qui a ete choisi dans la liste deroulante'})
    ##
    project_context = TextAreaField('Project context :*', validators=[DataRequired(), Length(min=10, max=1000)],
                                    render_kw={'placeholder': 'Explications generale du contexte lie au projet (ex : expliquer la raison d\'etre du projet, experiences ou publications anterieures, explications generales sur la maladie, etc.)'})
    project_summary = TextAreaField('Project summary :*', validators=[DataRequired(), Length(min=10, max=1000)],
                                    render_kw={'placeholder': 'Resume du projet en lui-meme, objectifs vises, etc.'})
    bioF_needs = TextAreaField('Needs for analysis and expertise in bioinformatics and biostatistics :*', validators=[DataRequired()],
                               render_kw={'placeholder': 'Techniques, outils, types de resultats, etc.'})
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
                           render_kw={'placeholder': 'Approximative, en GO'})
    add_info = TextAreaField('Additional informations if needs :',
                             render_kw={'placeholder': 'Exemple: biblio, precision(s) non renseignees(s) sans les precedents champs, valorisation(s) experee(s) (ex: publication), etc.'})

    submit = SubmitField('Send and get your project recap')


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
    urgency_of_request = SelectField('Urgency of request :', choices=[('Not urgent', 'Not urgent'),
                                                                      ('Not particularly urgent', 'Not particularly urgent'),
                                                                      ('Very urgent', 'Very urgent')
                                                                      ])
    if_urgency = TextAreaField('If very urgent, briefly explain the issues :', validators=[Length(min=2, max=50)])
    ##
    project_context = TextAreaField('Project context :', validators=[DataRequired(), Length(min=10, max=100)])
    project_summary = TextAreaField('Project summary :', validators=[DataRequired(), Length(min=10, max=100)])
    bioF_needs = TextAreaField('Needs for analysis and expertise in bioinformatics and biostatistics :', validators=[DataRequired()])
    data_available = BooleanField('Data is available and accessible?', validators=[DataRequired()])
    access_data = StringField('How can we access data? ', validators=[DataRequired()])
    data_owner = StringField('Data owner :', validators=[DataRequired()])
    regulatory_requirements = BooleanField('Regulatory requirements are available?')
    if_regulatory_requirements = SelectField('If yes, precise : ', choices=[('CPP', 'CPP'),
                                                                            ('Ethical Comity', 'Ethical Comity'),
                                                                            ('Jarde law conformity', 'Jarde law conformity'),
                                                                            ('Other', 'Other')
                                                                            ])
    data_type = StringField('Data type (eg, fastq, count table, bam ...): ', validators=[DataRequired(), Length(min=2, max=10)])
    data_size = FloatField('Data size (GO) :', validators=[validators.InputRequired(), validators.NumberRange(min=0, max=1000)])
    add_info = TextAreaField('Additional informations if needs (eg, biblio): ')

    submit = SubmitField('Validate and Send')
    

# project
class RequestProjectForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request project Sending')

    def validate_email(self, email):
        user = User.query.filter_by(email= email.data).first()
        if user is None:
            raise ValidationError('There is no account with this email. You must register first!') #template of validation method