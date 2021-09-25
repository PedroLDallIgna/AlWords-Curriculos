from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField, SelectField
from wtforms.fields.html5 import EmailField, TelField
from wtforms.validators import DataRequired, EqualTo

class SignUp(FlaskForm):
    name = StringField(label='Nome', validators=[DataRequired()])
    last_name = StringField(label="Sobrenome", validators=[DataRequired()])
    email = EmailField(label="Email", validators=[DataRequired(), EqualTo('confirm_email')])
    confirm_email = EmailField(label="Confirme o Email", validators=[DataRequired()])
    password = PasswordField(label="Senha", validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField(label="Confirme a Senha", validators=[DataRequired()])
    sex = SelectField(label="Sexo", choices=[('M', 'Masculino'), ('F', 'Feminino')], validators=[DataRequired()])
    # sex = RadioField(label="Sexo", choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    phone = TelField(label="Telefone", validators=[DataRequired()])
    submit = SubmitField("Cadastrar")

class SignIn(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")
