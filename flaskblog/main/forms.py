from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



# search form
class SearchForm(FlaskForm):
    searched = StringField('Recherché', validators=[DataRequired()])
    submit = SubmitField('Soumettre')
