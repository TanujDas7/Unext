from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    pet_name = StringField('Name of your pet', validators=[DataRequired(), Length(max=20)])
    pet_breed = StringField('Breed of your pet', validators=[Length(max=20)])
    pet_owner = StringField("Your name", validators=[DataRequired(), Length(max=20)])
    submit = SubmitField("Submit")

class UpdateForm(FlaskForm):
    petname = StringField('Name of your pet', validators=[Length(max=20)])
    petbreed = StringField('Breed of your pet', validators=[Length(max=20)])
    petowner = StringField("Pet owner", validators=[Length(max=20)])
    submit = SubmitField("Submit")

