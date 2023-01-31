from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField, BooleanField, RadioField
from wtforms.validators import DataRequired, InputRequired


#class of the form 
class TestForm(FlaskForm):
    type_property = RadioField("What is the property type ?", 
                               choices=['house','apartement'], 
                               validators=[InputRequired()])
    provinces = RadioField("What is the province ?", 
                               choices=['Luxembourg','Liege','Namur'], 
                               validators=[InputRequired()])
    building_state = RadioField("What is the state ?", 
                               choices=['To renovate','Renovated','New'], 
                               validators=[InputRequired()])
    fire_place = BooleanField("Fire place ?", default='checked')
    kitchen = BooleanField("is the kitchen fully equiped ?", 
                           default='checked')
    furnished = BooleanField("furnished ?", default='checked')
    garden = BooleanField("is there a garden ?", default='checked')
    swim = BooleanField("swimmingpool ?", default='checked')
    terrace = BooleanField("terrace ?", default='checked')

    number_bedroom = IntegerField("Number of rooms ?", validators=[DataRequired()])
    living_area = IntegerField("Living area ?", validators=[DataRequired()])
    facades_number = IntegerField("Number of facades ?", validators=[DataRequired()])

    submit = SubmitField("submit")