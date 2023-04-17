from flask import Blueprint, redirect, url_for
from flask import render_template, flash, Blueprint
from flaskblog.projects.forms import ProjectForm, GrantForm
from flask_login import current_user
from flaskblog.models import User
from flaskblog.projects.utils import send_recap_project, extract_form_info

projects = Blueprint('projects', __name__)

@projects.route("/project", methods=['GET', 'POST'])
def project():
    form = ProjectForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        #TODO function thetextract forminfo (form=form)
        dico = extract_form_info(form)
        send_recap_project(user, body=dico, form= form)
        flash('An email has been sent with recap project', 'info')
        return render_template('recapProject.html', title='project', form=form)
    return render_template('project.html', title='Project', form=form)


@projects.route("/grant", methods=['GET', 'POST'])
def grant():
    form = GrantForm()
    if form.validate_on_submit():
        flash(f'writing assistance {form.projectTitle.data} was created!', 'success')
        return render_template('recapGrant.html', title='grant', form=form)
    return render_template('grant.html', title='grant', form=form)