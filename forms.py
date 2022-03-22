from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class URLForm(FlaskForm):

    # url form that gets the url to be shortened
    url = StringField("URL", validators=[DataRequired(), URL()])
    submit = SubmitField("Shorten URL")