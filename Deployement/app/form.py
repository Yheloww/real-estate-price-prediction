from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, BooleanField, RadioField, SelectField
from wtforms.validators import DataRequired, InputRequired


# class of the form
class TestForm(FlaskForm):

    """
    instance of a form 
    control different aspect of the form 
    """
    # select field to make dropdown
    type_property = SelectField("What is the property type ?",
                                choices=['house', 'apartement'],
                                validators=[InputRequired()])
    provinces = SelectField("What is the province ?",
                            choices=['Luxembourg', 'Liege', 'Namur', 'Anvers', 'Brussel', 'E.Flanders', 'F.Brabant',
                                     'Hainaut', 'Limbourg', 'W.Flanders', 'W.brabant'],
                            validators=[InputRequired()])
    building_state = SelectField("What is the state ?",
                                 choices=['To renovate', 'Just renovated',
                                          'As new', 'To be done up', 'To restore', 'Good'],
                                 validators=[InputRequired()])
    # boolean field to maker checker
    fire_place = BooleanField("Fire place ?")
    kitchen = BooleanField("is the kitchen fully equiped ?")
    furnished = BooleanField("furnished ?")
    garden = BooleanField("is there a garden ?")
    swim = BooleanField("swimmingpool ?")
    terrace = BooleanField("terrace ?")
    # integer field for field to fill
    number_bedroom = IntegerField(
        "Number of rooms ?", validators=[DataRequired()])
    living_area = IntegerField("Living area ?", validators=[DataRequired()])
    facades_number = IntegerField(
        "Number of facades ?", validators=[DataRequired()])

    submit = SubmitField("submit")
