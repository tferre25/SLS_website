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
                  sender='helpbioinfo@sls.aphp.fr',
                  recipients=[user.email])
    msg.body = f''' 
            Pour réinitialiser votre mot de passe, visitez le lien suivant:
            {url_for('users.reset_token', token=token, _external = True)}
            Si vous n'avez pas fait cette demande, ignorez simplement cet e-mail et aucun changement ne sera effectué.
    '''
    
    mail.send(msg)
    
        
def send_project_request(project, form, request):
    msg = Message(f"Confirmation d'Acceptation de Votre Projet < {project.project_title} > | {form.asking_for.data}",
                  sender='helpbioinfo@sls.aphp.fr',
                  # COMMISSION RECHERCHE
                  cc = ['dina.ouahbi@aphp.fr',
                        request.author.email], #PERSONNE AYANT ACCEPTER LE PROJET
                  recipients=[project.email])
    msg.body= f'''
                Cher(e) {project.username},
                Nous avons le plaisir de vous informer que votre projet {project.project_title} a été < {form.project_request.data} > par notre équipe de sélection. Nous tenons à vous féliciter pour votre travail acharné et pour la qualité de votre proposition.
                Votre projet a suscité un grand intérêt parmi notre comité d'évaluation, et nous croyons fermement en son potentiel de succès. Nous sommes impatients de collaborer avec vous pour concrétiser cette idée innovante.

                Voici quelques informations importantes pour la suite du processus :

                    1. La personne qui va s'occuper de l'analyse < {request.author.email} > vous contactera dans les prochains jours pour discuter des détails pratiques liés à la mise en œuvre de votre projet. N'hésitez pas à poser toutes les questions que vous pourriez avoir lors de cet entretien.

                    2. Vous recevrez une invitation pour integrer un espace de travail WIMI qui sera dedier entierement à ce projet. 

                    3. Si vous avez besoin de ressources supplémentaires pour mener à bien votre projet, veuillez nous en informer dès que possible. Nous ferons de notre mieux pour vous fournir les ressources nécessaires.

                Sincères salutations,
                HelpBioinfo SLS,
            '''
    mail.send(msg)




