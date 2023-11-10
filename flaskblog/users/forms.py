from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField("Nom d'utilisateur", # html label
                           validators=[DataRequired(), Length(min=2, max=20)],
                           render_kw={'placeholder': 'firstName & lastName'}) #list of validations that we want to check
    email = StringField('E-mail',
                        validators=[DataRequired(), Email()],
                        render_kw={'placeholder': 'firstName.lastName@aphp.fr'})
    aphp_num = StringField('Numéro APHP',
                        validators=[DataRequired(), Length(min=7, max=10)],
                        render_kw={'placeholder': '1234567'})
    status = StringField('Status',
                         validators=[DataRequired(), Length(min=2)],
                         render_kw={'placeholder': 'Engineer; Medical intern...'})
    password = PasswordField('Mot de passe', 
                             validators=[DataRequired(),
                                         Length(min=8, max=16),
                                         Regexp(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).+$',
                                                message="""Le mot de passe doit contenir au moins une lettre majuscule, 
                                                une lettre minuscule et un chiffre..""")],
                             render_kw={'placeholder': '**************'})
    confirm_password = PasswordField('Confirmer le mot de passe',
                                     validators=[DataRequired(), EqualTo('password')],
                                     render_kw={'placeholder': '**************'})
    submit = SubmitField("S'inscrire")

    def validate_username(self, username):
        user = User.query.filter_by(username= username.data).first()
        if user:
            raise ValidationError("Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre") #template of validation method
        
    def validate_email(self, email):
        user = User.query.filter_by(email= email.data).first()
        if user:
            raise ValidationError("L'adresse électronique de l'utilisateur est déjà utilisée. Veuillez en choisir un autre") #template of validation method

class UpdateAccountForm(FlaskForm):
    username = StringField("Nom d'utilisateur", # html label
                           validators=[DataRequired(), Length(min=2, max=20)]) #list of validations that we want to check
    email = StringField('E-mail',
                        validators=[DataRequired(), Email()])
    aphp_num = StringField('Numéro APHP',
                        validators=[DataRequired(), Length(min=7, max=10)])
    status = StringField('Status',
                         validators=[DataRequired(), Length(min=2)])
    picture = FileField("Mise à jour de l'image du profil", validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Mise à jour')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username= username.data).first()
            if user:
                raise ValidationError("Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre") #template of validation method
        
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email= email.data).first()
            if user:
                raise ValidationError("The user's e-mail address is already in use. Please choose another one") #template of validation method


class LoginForm(FlaskForm):
    email = StringField('E-mail',validators=[DataRequired(), Email()], render_kw={'placeholder': 'firstName.lastName@aphp.fr'})
    password = PasswordField('Mot de passe', validators=[DataRequired()], render_kw={'placeholder': '**********************'})
    remember = BooleanField("Souvenez-vous de moi") #remember the password
    submit = SubmitField('Connexion')


class RequestResetForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()], render_kw={'placeholder': 'firstName.lastName@aphp.fr'})
    submit = SubmitField("Demande de réinitialisation du mot de passe")

    def validate_email(self, email):
        user = User.query.filter_by(email= email.data).first()
        if user is None:
            raise ValidationError("Il n'y a pas de compte avec cet email. Vous devez d'abord vous inscrire !") #template of validation method
        
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Mot de passe', 
                             validators=[DataRequired(),
                                         Length(min=8, max=16),
                                         Regexp(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).+$',
                                                message="""Le mot de passe doit contenir au moins une lettre majuscule,
                                                une lettre minuscule et un chiffre.""")],
                             render_kw={'placeholder': '**************'})
    confirm_password = PasswordField('Confirmer le mot de passe',
                                     validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Réinitialiser le mot de passe')


class ProjectRequestForm(FlaskForm):
    project_id = StringField('Identifiant du projet : *', validators=[DataRequired()], render_kw={'placeholder': 'eg, 5edffc5d29b070cac566f69d04bb63c0db5119837284f6fa84db7da1442b30a7'})
    asking_for = SelectField('Demande de : *', validators=[DataRequired()], choices=[('Funding','Financement'),
                                                                                     ('Requiring bioinformatics support',"Nécessitant un soutien bioinformatique")])
    project_request = SelectField('Demande de projet : *', choices=[('Accepted', 'Accepté'),('Refused', 'Refusé')])
    motif = StringField('Motif : ', render_kw={'placeholder': "Exemple, cela ne concerne pas mes attributs . . ."})
    submit = SubmitField('Envoyer')


class ProjectProgressForm(FlaskForm):
    project_id = StringField('Identifiant du projet : *', validators=[DataRequired()], render_kw={'placeholder': 'eg, 5edffc5d29b070cac566f69d04bb63c0db5119837284f6fa84db7da1442b30a7'})
    progress = SelectField('Niveau de progression : *', validators=[DataRequired()], choices=[('Collecte des données','Collecte des données'),
                                                                                              ('Nettoyage des données',"Nettoyage des données"),
                                                                                              ('Exploration des données',"Exploration des données"),
                                                                                              ("Choix de méthodes d'analyse","Choix de méthodes d'analyse"),
                                                                                              ("Conception de l'analyse","Conception de l'analyse"),
                                                                                              ("Analyse statistique","Analyse statistique "),
                                                                                              ("Interprétation des résultats","Interprétation des résultats"),
                                                                                              ("Rapport des résultats","Rapport des résultats"),
                                                                                              ("Validation et réplication","Validation et réplication"),
                                                                                              ("Discussion des implications","Discussion des implications"),
                                                                                              ("Méta-analyse (le cas échéant)","Méta-analyse (le cas échéant)"),
                                                                                              ("Préparation des données pour la publication","Préparation des données pour la publication"),
                                                                                              ("Révision par les pairs","Révision par les pairs"),
                                                                                              ("Publication","Publication"),
                                                                                              ("Mise à jour et suivi","Mise à jour et suivi")])
    submit = SubmitField('Ajouter')
     
