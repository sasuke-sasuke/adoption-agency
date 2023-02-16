from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class PetForm(FlaskForm):
    """Pet Form Template"""
    name = StringField('Pet Name', validators=[InputRequired(message='Name cant be blank')])
    species = StringField('Species', validators=[InputRequired(message='Must enter pets species'), AnyOf(values=['dog', 'cat', 'porcupine'], message='Must be dog, cat or porcupine')])
    photo_url = StringField('Photo URL', validators=[URL(message='Input must be a URL'), Optional()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30, message='Age must be between 0 - 30'), Optional()])
    notes = StringField('Notes', validators=[Optional()])


class EditPetForm(FlaskForm):
    """Edit Pet From Template"""
    photo_url = StringField('Photo URL', validators=[URL(message='Input must be a URL'), Optional()])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField("Is available?")