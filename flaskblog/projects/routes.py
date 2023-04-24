from flask import Blueprint, redirect, url_for
from flask import render_template, flash, Blueprint
from flaskblog.projects.forms import ProjectForm, GrantForm
from flask_login import login_required
from flaskblog.models import User, Project
from flaskblog import db, bcrypt
from flaskblog.projects.utils import send_recap_project, extract_form_info, object_project

projects = Blueprint('projects', __name__)

"""@projects.route("/project", methods=['GET', 'POST'])
@login_required
def project():
    form = ProjectForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        #TODO function thetextract forminfo (form=form)
        dico = extract_form_info(form)
        send_recap_project(user, body=dico, form= form)
        flash('An email has been sent with recap project', 'info')
        return render_template('recapProject.html', title='project', form=form)
    return render_template('project.html', title='Project', form=form)"""

@projects.route("/project", methods=['GET', 'POST'])
@login_required
def project():
    form = ProjectForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # ADD TO DATABASE
        project = object_project()
        db.session.add(project)
        db.session.commit()

        # SEND A RECAP EMAIL
        dico = extract_form_info(form)
        send_recap_project(user, body=dico, form= form)

        # REDIRECT
        flash('Your project was created succesfully & An email has been sent with recap project', 'info')
        return render_template('recapProject.html', title='project', form=form)
    return render_template('project.html', title='Project', form=form)

@projects.route("/project/<int:project_id>")
def project_unit(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_unit.html', title=project.project_title, project=project)


@projects.route("/grant", methods=['GET', 'POST'])
@login_required
def grant():
    form = GrantForm()
    if form.validate_on_submit():
        flash(f'writing assistance {form.projectTitle.data} was created!', 'success')
        return render_template('recapGrant.html', title='grant', form=form)
    return render_template('grant.html', title='grant', form=form)


