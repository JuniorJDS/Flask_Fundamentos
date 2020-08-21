from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired, Email


class ClientForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    email = EmailField("email", validators=[Email(), DataRequired()])
    data_nascimento = DateField("data_nascimento", validators=[DataRequired()])
    profissao = StringField("profissao", validators=[DataRequired()])
    sexo = SelectField("sexo", validators=[DataRequired()], choices=[('M', 'Masculino'), ('F', 'Feminino'),
                                                                     ('N', 'Nenhuma das opções')])
