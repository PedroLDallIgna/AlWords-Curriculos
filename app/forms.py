from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField, SelectField
from wtforms.fields.html5 import EmailField, TelField
from wtforms.validators import DataRequired, EqualTo

class SignUp(FlaskForm):
    name = StringField(label='Nome', validators=[DataRequired("Nome é um campo obrigatório!")])
    last_name = StringField(label="Sobrenome", validators=[DataRequired("Sobrenome é um campo obrigatório!")])
    email = EmailField(label="Email", validators=[DataRequired("Email é um campo obrigatório!"), EqualTo('confirm_email')])
    confirm_email = EmailField(label="Confirme o Email", validators=[DataRequired()])
    password = PasswordField(label="Senha", validators=[DataRequired("Senha é um campo obrigatório!"), EqualTo('confirm_password')])
    confirm_password = PasswordField(label="Confirme a Senha", validators=[DataRequired()])
    sex = SelectField(label="Sexo", choices=[('M', 'Masculino'), ('F', 'Feminino')], validators=[DataRequired("Sexo é um campo obrigatório!")])
    # sex = RadioField(label="Sexo", choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    phone = TelField(label="Telefone", validators=[DataRequired("Telefone é um campo obrigatório!")])
    submit = SubmitField("Cadastrar")

class SignIn(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired("Email é um campo obrigatório!")])
    password = PasswordField(label="Senha", validators=[DataRequired("Senha é um campo obrigatório!")])
    submit = SubmitField("Entrar")
