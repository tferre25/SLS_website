import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flaskblog import mail
from flask import current_app
import socket
from itsdangerous import URLSafeTimedSerializer


def save_picture(form_picture):
    random_hex= secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename) #get filename and extension
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    # resize image ==> speed up website
    #output_size = (125, 125)
    i = Image.open(form_picture)
    #i.thumbnail(output_size)
    i.save(picture_path)
    #retun filename image
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f''' 
            Pour réinitialiser votre mot de passe, visitez le lien suivant:
            {url_for('users.reset_token', token=token, _external = True)}
            Si vous n'avez pas fait cette demande, ignorez simplement cet e-mail et aucun changement ne sera effectué.
    '''
    
    mail.send(msg)
    
        

def send_project_request(project, form, request):
    msg = Message(f'Réponse à votre projet "{project.project_title}" | {form.asking_for.data}',
                  sender='noreply@demo.com',
                  recipients=[project.email])
    msg.body= f'''
            Cher {project.username},
            Votre projet a été {form.project_request.data}
            Le motif était : {form.motif.data}

            La personne qui s'occupera de votre projet : {request.author.email}

            Salutations, 
            Equipe des bioinformaticiens de l'APHP - SLS, 

    '''
    mail.send(msg)




