from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed


class PostForm(FlaskForm):
    title = StringField('Titre', validators=[DataRequired()])
    content = TextAreaField('Contenu', validators=[DataRequired()])
    image_file = FileField("Mise à jour de l'image du poste", validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Poster')


class CommentForm(FlaskForm):
    comment = StringField('Commentaire',validators=[DataRequired()], render_kw={'placeholder': 'Votre avis'})
    submit = SubmitField('Ajouter')

