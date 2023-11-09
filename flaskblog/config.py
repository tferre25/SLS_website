import os


def get_admins():
    my_admins = [
        'samuel.quentin@aphp.fr',
        'dina.ouabhi@aphp.fr',
        'julien.robert@aphp.fr',
        'abdeljalil.senhajirachik@aphp.fr',
        'maud.salmona@aphp.fr',
        'theo.ferreira@aphp.fr'
        ]
    return my_admins

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.aphp.fr' #'smtp.googlemail.com' 
    MAIL_PORT = 25 #587 
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASK_APP = os.environ.get('FLASK_APP')

    

