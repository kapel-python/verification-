from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class EmailForm(FlaskForm):
    """Form for email input and validation."""
    email = StringField('Email', validators=[
        DataRequired(message='Требуется указать email'),
        Email(message='Пожалуйста, введите корректный email адрес')
    ])
    submit = SubmitField('Отправить код')
