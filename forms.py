from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

class PizzaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    direccion = StringField('Dirección', validators=[DataRequired()])
    telefono = StringField('Teléfono', validators=[DataRequired()])
    tamano = SelectField('Tamaño de la pizza', choices=[
        ('chica', 'Chica - $40'),
        ('mediana', 'Mediana - $80'),
        ('grande', 'Grande - $120')
    ], validators=[DataRequired()])
    jamon = BooleanField('Jamón')
    pina = BooleanField('Piña')
    champinones = BooleanField('Champiñones')
    numero = IntegerField('Cantidad', validators=[DataRequired()])
    submit = SubmitField('Calcular total')
