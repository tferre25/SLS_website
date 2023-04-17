from flask import url_for
from flask_mail import Message
from flaskblog import mail
import re, os
from email.mime.image import MIMEImage


def send_recap_project(user, body, form):
    token = user.get_reset_token()
    msg = Message('Summary of your project',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f"""
    Hello {user.username.capitalize()},

    Following your request for assistance for the project entitled "{form.project_title.data.capitalize()}", 
    please find below a summary of the points summarizing the different criteria of the project : 
                
                {body}

    If you have any questions, do not hesitate to come back on the contact page by clicking on the link below.
                
    {url_for('main.about', token=token, _external = True)}

    You can check out our team projects in Github by clicking on the link bellow.

    https://github.com/bioinformatic-hub-sls

    APHP Team
    Regards,
    
    """
    
    
    mail.send(msg)

def extract_label(s):
    matches = re.findall('"([^"]*)"', str(s))
    return matches[0]

def extract_form_info(form):
    body = f'''

        {extract_label(form.username.label)}\t:\t{form.username.data} \n
        {extract_label(form.email.label)}\t:\t{form.email.data} \n
        {extract_label(form.project_title.label)}\t:\t{form.project_title.data} \n
        {extract_label(form.organism.label)}\t:\t{form.organism.data} \n

                ***************************************

        {extract_label(form.principal_investigator.label)}\t:\t{form.principal_investigator.data} \n
        {extract_label(form.promotor.label)}\t:\t{form.promotor.data} \n
        {extract_label(form.urgency_of_request.label)}\t:\t{form.urgency_of_request.data} \n
        {extract_label(form.if_urgency.label)}\t:\t{form.if_urgency.data} \n

                ***************************************

        {extract_label(form.project_context.label)}\t:\t{form.project_context.data} \n
        {extract_label(form.project_summary.label)}\t:\t{form.project_summary.data} \n
        {extract_label(form.bioF_needs.label)}\t:\t{form.bioF_needs.data} \n
        {extract_label(form.data_available.label)}\t:\t{form.data_available.data} \n

                ***************************************

        {extract_label(form.access_data.label)}\t:\t{form.access_data.data} \n
        {extract_label(form.data_owner.label)}\t:\t{form.data_owner.data} \n
        {extract_label(form.regulatory_requirements.label)}\t:\t{form.regulatory_requirements.data} \n
        {extract_label(form.if_regulatory_requirements.label)}\t:\t{form.if_regulatory_requirements.data} \n

                ***************************************

        {extract_label(form.data_type.label)}\t:\t{form.data_type.data} \n
        {extract_label(form.data_size.label)}\t:\t{form.data_size.data} \n
        {extract_label(form.add_info.label)}\t:\t{form.add_info.data} \n
    '''
    return body


