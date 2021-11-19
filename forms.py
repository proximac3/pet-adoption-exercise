from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, AnyOf

class AddPetForm(FlaskForm):
    """Form For Adding Pet"""

    name = StringField("Name of pet", validators=[InputRequired(message="Pet name cannot be empty")])

    species = StringField("Species of Pet", validators=[InputRequired(message="Species cannot be empty"), AnyOf(values=['cat', 'dog', 'porcupine'], message="Species must be either cat, dog or porcupine")])

    photo_url = StringField("Url of Pet", validators=[Optional()])

    age = IntegerField("Age of Pet", validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])

    notes = StringField("Notes about pet")

    available = BooleanField("Check if pet is Available for Adoption" )







