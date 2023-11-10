import os
import secrets
from PIL import Image
from flask_mail import Message
from flask import current_app
from flaskblog import mail
from flaskblog.models import User
from flask import flash
import smtplib


def save_picture(form_picture):
    random_hex= secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename) #get filename and extension
    if f_ext.lower() not in ('.jpg', '.jpeg', '.png', '.gif'):
        raise ValueError('Invalid file extension')
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    # resize image ==> speed up website
    #output_size = (300, 500)
    #i = Image.open(form_picture)
    #i.thumbnail(output_size)
    form_picture.save(picture_path)
    #retun filename image
    return picture_fn


def send_post_email(user):
    #token = user.get_reset_token()
    try:
        users = User.query.all()
        emails = [u.email for u in users] # un get de tout les utilisateur
        msg = Message(f'Nouveau post de {user.username}',
                    sender='helpbioinfo@sls.aphp.fr',
                    #cc = [form.email.data],
                    recipients=emails)
        msg.body = f"""
                    Cher(e) abonné(e),

                    Nous sommes heureux de vous informer qu'un de nos utilisateurs, {user.username}, a publié un nouveau post sur notre plateforme. Ne manquez pas cette occasion de découvrir son contenu!

                    Découvrez le post de {user.username} en cliquant sur le lien ci-dessous :
                    http://bioinfo-recherche.sls.aphp.fr/home

                    N'hésitez pas à interagir avec le post en partageant vos réflexions avec la communauté.

                    Merci de nous suivre et de soutenir nos utilisateurs.

                    Cordialement,
                    Equipe HelpBioinfo SLS
        """
        mail.send(msg)
    except smtplib.SMTPNotSupportedError:
        flash(f'Vérifier votre connextion internet !', 'warning')