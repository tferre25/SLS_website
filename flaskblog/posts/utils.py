import os
import secrets
from PIL import Image
from flask_mail import Message
from flask import current_app



def save_picture(form_picture):
    random_hex= secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename) #get filename and extension
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    # resize image ==> speed up website
    output_size = (300, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    #retun filename image
    return picture_fn