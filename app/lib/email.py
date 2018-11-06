
from app import mail
from flask_mail import Message
from flask import current_app,render_template

def send_mail(to,subject,template,**kwargs):
    msg = Message('[鱼书]' + ' ' + subject,
                  sender=current_app.config['MAIL_USERNAME'], recipients=[to])
    # msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    # thr = Thread(target=send_async_email, args=[app, msg])
    # thr.start()
    pass