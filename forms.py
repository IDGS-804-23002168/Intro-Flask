from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField
from wtforms.validators import DataRequired, Email

class UserForm(FlaskForm):
    matricula = IntegerField(
        "Matricula",
        validators=[DataRequired(message="El campo es requerido")]
    )

    nombre = StringField(
        "Nombre",
        validators=[DataRequired(message="El campo es requerido")]
    )

    apellido = StringField(
        "Apellido",
        validators=[DataRequired(message="El campo es requerido")]
    )

    correo = EmailField(
        "Email",
        validators=[
            DataRequired(message="El campo es requerido"),
            Email(message="Ingresa un correo válido")
        ]
    )