from wtforms import Form,StringField,IntegerField,PasswordField
from wtforms.validators import Length,NumberRange,DataRequired,Email,ValidationError

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),Email(message='电子邮件不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不为空'),Length(6,32)])
    nickname = StringField(validators=[DataRequired(),Length(2,30,message='2-10')])

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('昵称已被注册')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),Email(message='电子邮件不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不为空'),Length(6,32)])

class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8,64),Email(message='电子邮件不符合规范')])