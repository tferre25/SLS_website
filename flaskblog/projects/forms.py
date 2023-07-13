from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, BooleanField, FloatField, validators, DateField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from flaskblog.models import User
from datetime import datetime

laboratories = [('Bactériologie','Bactériologie'),
               ('Biochimie','Biochimie'),
               ('Biologie cellulaire','Biologie cellulaire'),
               ('Diagnostic biologique automatisé','Diagnostic biologique automatisé'),
               ('Génétique neurovasculaire','Génétique neurovasculaire'),
               ('Hématologie','Hématologie'),
               ('HLA','HLA'),
               ('Immunocellulaire','Immunocellulaire'),
               ('Immunopathologie', 'Immunopathologie'),
               ('Oncologie moléculaire', 'Oncologie moléculaire'),
               ('Parasitologie - Mycologie', 'Parasitologie - Mycologie'),
               ('Pharmacogénétique','Pharmacogénétique'),
               ('Pharmacogénomique', 'Pharmacogénomique'),
               ('Pharmacologie biologique', 'Pharmacologie biologique'),
               ('Virologie', 'Virologie')]

laboratories.sort(key=lambda x: x[1])
laboratories.append(('Autre', 'Autre'))

funding = [('PHRC-R','PHRC-R'),
           ('PHRC-N','PHRC-N'),
           ('PRZK','PRZK'),
           ('PRME','PRME'),
           ('ANR','ANR'),
           ('INCA','INCA'),
           ]


funding.sort(key=lambda x: x[1])
funding.append(('Autre', 'Autre'))


# TO USE IT IN GRANT FORM 
class CustomDateField(StringField):
    def process_formdata(self, valuelist):
        if valuelist:
            date_string = valuelist[0]
            try:
                self.data = datetime.strptime(date_string, "%d-%m-%Y").date()
            except ValueError:
                raise ValueError("Format de date non valide, veuillez utiliser DD-MM-YYYY")
        else:
            self.data = None

class ProjectForm(FlaskForm):  
    username = SelectField('Vous êtes* :', choices=[(None,None),
                                                  ('Laboratoire diagnostic St Louis', 'Laboratoire diagnostic St Louis'),
                                                  ('Service clinique St Louis', 'Service clinique St Louis')],
                                        validators=[DataRequired()])
    application = SelectField('Application :', choices=[('For_research', 'Recherche'),('For_diagnosis', 'Diagnostic(routine)')]) # if username = 'Laboratoire diagnostic St Louis
    laboratories = SelectField("Services cliniques de Saint-Louis", choices=laboratories)# if username = 'Laboratoire diagnostic St Louis
    if_no_laboratory = StringField('Précisez quel laboratoire:',render_kw={'placeholder': 'cardio, reanimation...'}) # if laboratories = 'autre'
    clinical_service = StringField('Service clinique :',render_kw={'placeholder': 'cardio, reanimation...'}) # if username= Service clinique St Louis
    email = StringField('E-mail (personne à copier) :', validators=[Email()],render_kw={'placeholder': 'firstName.lastName@aphp.fr'})
    project_title = StringField('Titre du projet :*', validators=[DataRequired(), Length(min=2)],render_kw={'placeholder': 'Nom du projet'})
    organism = StringField('Organisme (financement succeptible) :',render_kw={'placeholder': 'Structure ou organisation finançant le projet'})
    principal_investigator = StringField('Investigateur principal :',render_kw={'placeholder': 'nom et prénom'})
    promotor = StringField('Promoteur :',render_kw={'placeholder': 'Noms des promoteurs (ex: APHP, DRCI)'})
    data_available = SelectField('Les données sont disponibles?:', choices=[('No', 'Non'),('Yes', 'Oui')])
    access_data = StringField('Si disponible, veuillez préciser : ',render_kw={'placeholder': 'Comment accéder aux données? '})
    add_info = TextAreaField('Informations complémentaires si nécessaire :',render_kw={'placeholder': 'Example: biblio, precision(s), Publication etc.'})
    urgency_of_request = SelectField('Urgency of request :', choices=[('Not urgent', 'Non urgent'),
                                                                      ('Not particularly urgent', "Pas d'urgence particulière"),
                                                                      ('Very urgent', 'Trés urgent')
                                                                      ])
    if_urgency = TextAreaField("Si c'est très urgent, veuillez expliquer brièvement les problèmes. :",render_kw={'placeholder': "Expliquer la raison de l'urgence, en fonction de ce qui a été sélectionné dans la liste déroulante"})
    project_context = TextAreaField('Contexte du projet :*', validators=[DataRequired(), Length(min=10)],render_kw={'placeholder': "Explications générales du contexte du projet (ex : expliquer la raison d'être du projet, expériences ou publications antérieures, explications générales sur la maladie, etc.)"})
    project_context_private = TextAreaField('Contexte du projet privé:',render_kw={'placeholder': "Explications générales du contexte du projet (ex : expliquer la raison d'être du projet, expériences ou publications antérieures, explications générales sur la maladie, etc.)"})
    project_summary = TextAreaField('Résumé du projet:*', validators=[DataRequired(), Length(min=10)],render_kw={'placeholder': 'Résumé du projet lui-même, des objectifs, etc.'})
    bioF_needs = TextAreaField("Besoins d'analyse et d'expertise en bioinformatique et biostatistique :*", validators=[DataRequired()],render_kw={'placeholder': "Analyse; Développement de logiciels; etc."})
    data_owner = StringField('Propriétaire des données :*', validators=[DataRequired()],render_kw={'placeholder': 'Qui possède les données ?'})
    regulatory_requirements = SelectField('Les exigences réglementaires sont-elles disponibles ?:', choices=[('No', 'Non'),('Yes', 'Oui')])
    if_regulatory_requirements = SelectField('Si des exigences réglementaires sont disponibles, veuillez préciser : ', choices=[('CPP', 'CPP'),
                                                                                                                    ('Ethical Comity', "Comités d'éthique"),
                                                                                                                    ('Jarde law conformity', 'Conformité de la loi Jarde'),
                                                                                                                    ('Other', 'Autres')
                                                                                                                    ])
    data_type = StringField('Type de donnée :*', validators=[DataRequired(), Length(min=2)],render_kw={'placeholder': 'ex: fastq, counting tables, bam, etc.'})
    data_size = FloatField('Taille de donnée (GO) :*', validators=[validators.InputRequired(), validators.NumberRange(min=0)],render_kw={'placeholder': 'Approximate, in GO'})
    
    submit = SubmitField('Soumettre')

class GrantForm(FlaskForm):  
    username = SelectField('Vous êtes* :', choices=[(None,None),
                                                  ('Laboratoire diagnostic St Louis', 'Laboratoire diagnostic St Louis'),
                                                  ('Service clinique St Louis', 'Service clinique St Louis')],
                                        validators=[DataRequired()])
    application = SelectField('Application:', choices=[('For_research', 'Recherche')]) # if username = 'Laboratoire diagnostic St Louis
    laboratories = SelectField('Services cliniques de Saint-Louis', choices=laboratories)# if username = 'Laboratoire diagnostic St Louis
    if_no_laboratory = StringField('Précisez quel laboratoire:',render_kw={'placeholder': 'cardio, reanimation...'}) # if laboratories = 'autre'
    clinical_service = StringField('Service clinique:',render_kw={'placeholder': 'cardio, reanimation...'}) # if username= Service clinique St Louis

    # REQUIRED
    email = StringField('E-mail (personne à copier):', validators=[Email()],render_kw={'placeholder': 'firstName.lastName@aphp.fr'})
    project_title = StringField('Title du projet:*', validators=[DataRequired(), Length(min=2)],render_kw={'placeholder': 'Nom du projet'})
    organism = StringField('Organisme (financement succeptible):',render_kw={'placeholder': 'Structure ou organisation finançant le projet'})
    principal_investigator = StringField('Investigateur principal:',render_kw={'placeholder': 'Nom et prénom'})
    promotor = StringField('Promoteur :',render_kw={'placeholder': 'promoteur(s) names (ex: APHP, DRCI)'})
    data_available = SelectField('Les données sont disponibles?:', choices=[('No', 'Non'),('Yes', 'Oui')])
    access_data = StringField('if available, please precise :',render_kw={'placeholder': 'How can we access data? '})
    add_info = TextAreaField('Informations complémentaires si nécessaire :',render_kw={'placeholder': 'Example: biblio, precisions publication etc.'})
    urgency_of_request = SelectField('Urgency of request :', choices=[('Not urgent', 'Non urgent'),
                                                                      ('Not particularly urgent', "Pas d'urgence particulière"),
                                                                      ('Very urgent', 'Trés urgent')
                                                                      ])
    if_urgency = TextAreaField("Si c'est très urgent, veuillez expliquer brièvement les problèmes:",render_kw={'placeholder': "Expliquer la raison de l'urgence, en fonction de ce qui a été sélectionné dans la liste déroulante"})
    project_context = TextAreaField('Contexte du projet :*', validators=[DataRequired(), Length(min=10)],render_kw={'placeholder': "Explications générales du contexte du projet (ex : expliquer la raison d'être du projet, expériences ou publications antérieures, explications générales sur la maladie, etc.)"})
    project_context_private = TextAreaField('Contexte privé du projet:', render_kw={'placeholder': "Explications générales du contexte du projet (ex : expliquer la raison d'être du projet, expériences ou publications antérieures, explications générales sur la maladie, etc.)"})
    project_summary = TextAreaField('Résumé du projet :*', validators=[DataRequired(), Length(min=10)],render_kw={'placeholder': 'Résumé du projet lui-même, des objectifs, etc.'})
    bioF_needs = TextAreaField("Besoins d'analyse et d'expertise en bioinformatique et biostatistique:*", validators=[DataRequired()],render_kw={'placeholder': 'Analyse; Développement de logiciels; etc.'})
    data_owner = StringField('Propriétaire des données:*', validators=[DataRequired()],render_kw={'placeholder': 'Qui possède les données ??'})
    
    regulatory_requirements = SelectField('Les exigences réglementaires sont disponibles?:', choices=[('No', 'Non'),('Yes', 'Oui')])
    if_regulatory_requirements = SelectField('Si des exigences réglementaires sont disponibles, veuillez préciser:', choices=[('CPP', 'CPP'),
                                                                                                                    ('Ethical Comity', "Comités d'éthique"),
                                                                                                                    ('Jarde law conformity', 'Conformité de la loi Jarde'),
                                                                                                                    ('Other', 'Autres')
                                                                                                                    ])
    data_type = StringField('Type de donnée :*', validators=[DataRequired(), Length(min=2)],render_kw={'placeholder': 'ex: fastq, counting tables, bam, etc.'})
    data_size = FloatField('Taille de donnée (GO) :*', validators=[validators.InputRequired(), validators.NumberRange(min=0)],render_kw={'placeholder': 'Approximate, in GO'})
    funding_type = SelectField('Type de financement : *',choices=funding, validators=[DataRequired()], render_kw={'placeholder': 'Type de financement ...'})
    total_amount = FloatField('Montant total: *', validators=[DataRequired()],render_kw={'placeholder': 'Montant total ...'})
    deadline = CustomDateField('Date limite: *', validators=[DataRequired()],render_kw={'placeholder': 'please use DD-MM-YYYY'})

    submit = SubmitField('Soumettre')

# project
class RequestProjectForm(FlaskForm):
    email = StringField('E-mail',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request project Sending')

    def validate_email(self, email):
        user = User.query.filter_by(email= email.data).first()
        if user is None:
            raise ValidationError('There is no account with this email. You must register first!') #template of validation method
        

