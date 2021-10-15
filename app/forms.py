from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField, SelectField, TextAreaField
from wtforms.fields.html5 import EmailField, TelField, IntegerField
from wtforms.validators import DataRequired, EqualTo

class SignUp(FlaskForm):
    name = StringField(label='Nome', validators=[DataRequired("Nome é um campo obrigatório!")])
    last_name = StringField(label="Sobrenome", validators=[DataRequired("Sobrenome é um campo obrigatório!")])
    email = EmailField(label="Email", validators=[DataRequired("Email é um campo obrigatório!"), EqualTo('confirm_email')])
    confirm_email = EmailField(label="Confirme o Email", validators=[DataRequired()])
    password = PasswordField(label="Senha", validators=[DataRequired("Senha é um campo obrigatório!"), EqualTo('confirm_password')])
    confirm_password = PasswordField(label="Confirme a Senha", validators=[DataRequired()])
    sex = SelectField(label="Sexo", choices=[('M', 'Masculino'), ('F', 'Feminino'), ('H', 'Helicóptero')], validators=[DataRequired("Sexo é um campo obrigatório!")])
    phone = TelField(label="Telefone", validators=[DataRequired("Telefone é um campo obrigatório!")])
    submit = SubmitField("Cadastrar")

class SignIn(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired("Email é um campo obrigatório!")])
    password = PasswordField(label="Senha", validators=[DataRequired("Senha é um campo obrigatório!")])
    submit = SubmitField("Entrar")

class EditProfile(FlaskForm):
    description = TextAreaField(label='Descrição')
    facebook = StringField(label='Facebook')
    instagram = StringField(label='Instagram')
    twitter = StringField(label='Twitter')
    linkedin = StringField(label='LinkedIn')
    github = StringField(label='GitHub')

class PersonalInfo(FlaskForm):
    name = StringField(label="Nome", validators=[DataRequired()])
    last_name = StringField(label="Sobrenome", validators=[DataRequired()])
    address = StringField(label="Endereço")

class AcademicDegree(FlaskForm):
    ad_begin1 = IntegerField(label="Ano de Início")
    ad_end1 = IntegerField(label="Ano de Conclusão")
    ad_degree1 = StringField(label="Formação")
    ad_begin2 = IntegerField(label="Ano de Início")
    ad_end2 = IntegerField(label="Ano de Conclusão")
    ad_degree2 = StringField(label="Formação")
    ad_begin3 = IntegerField(label="Ano de Início")
    ad_end3 = IntegerField(label="Ano de Conclusão")
    ad_degree3 = StringField(label="Formação")
    ad_begin4 = IntegerField(label="Ano de Início")
    ad_end4 = IntegerField(label="Ano de Conclusão")
    ad_degree4 = StringField(label="Formação")

class ComplementarDegree(FlaskForm):
    cd_begin1 = IntegerField(label="Ano de Início")
    cd_end1 = IntegerField(label="Ano de Conclusão")
    cd_degree1 = StringField(label="Formação")
    cd_begin2 = IntegerField(label="Ano de Início")
    cd_end2 = IntegerField(label="Ano de Conclusão")
    cd_degree2 = StringField(label="Formação")
    cd_begin3 = IntegerField(label="Ano de Início")
    cd_end3 = IntegerField(label="Ano de Conclusão")
    cd_degree3 = StringField(label="Formação")
    cd_begin4 = IntegerField(label="Ano de Início")
    cd_end4 = IntegerField(label="Ano de Conclusão")
    cd_degree4 = StringField(label="Formação")
