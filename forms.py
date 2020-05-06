from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField, SelectField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired


class AddFriendsForm(FlaskForm):
    request_id = StringField('Request number', validators=[DataRequired()])
    submit = SubmitField('Accept the request')


class DeleteForm(FlaskForm):
    submit = SubmitField('Delete a profile')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')


class ProfileForm(FlaskForm):
    submit = SubmitField('Publish profile')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    country = SelectField('Country', choices=[
        ('Is not specified', 'Is not specified'),
        ('Russia', 'Russia'),
        ('USA', 'USA'),
        ('Germany', 'Germany'),
        ('France', 'France'),
        ('Spain', 'Spain'),
        ('China', 'China'),
        ('Italy', 'Italy'),
        ('Great Britain', 'Great Britain'),
        ('Ukraine', 'Ukraine'),
        ('Japan', 'Japan'),
        ('Denmark', 'Denmark'),
        ('Norway', 'Norway'),
        ('South Korea', 'South Korea')
    ], default='Is not specified')
    sex = RadioField('Sex', choices=[('male', 'Male'), ('female', 'Female')], default='male')
    bio = TextAreaField('Bio', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_passw = PasswordField('Repeat password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RequestForm(FlaskForm):
    profile_id = StringField('Profile number', validators=[DataRequired()])
    submit = SubmitField('Send request')


class NotesForm(FlaskForm):
    header = StringField('Header', validators=[DataRequired()])
    note = TextAreaField('Note', validators=[DataRequired()])
    submit = SubmitField('Add a note')


class ParametersForm(FlaskForm):
    age_from = StringField('Age from')
    age_to = StringField('Age to')
    country = SelectField('Country', choices=[
        ('Is not specified', 'Is not specified'),
        ('Russia', 'Russia'),
        ('USA', 'USA'),
        ('Germany', 'Germany'),
        ('France', 'France'),
        ('Spain', 'Spain'),
        ('China', 'China'),
        ('Italy', 'Italy'),
        ('Great Britain', 'Great Britain'),
        ('Ukraine', 'Ukraine'),
        ('Japan', 'Japan'),
        ('Denmark', 'Denmark'),
        ('Norway', 'Norway'),
        ('South Korea', 'South Korea')
    ], default='not spec')
    sex = RadioField('Sex', choices=[('male', 'Male'), ('female', 'Female'), ('all', 'All')], default='all')
    submit = SubmitField('Sort profiles')
