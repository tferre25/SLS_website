from flask import Blueprint, redirect, url_for, abort, request
from flask import render_template, flash, Blueprint
from flaskblog.projects.forms import ProjectForm, GrantForm
from flask_login import login_required, current_user
from flaskblog.models import User, Project, Grant, Project_request
from flaskblog import db, admin_required
from flaskblog.projects.utils import send_recap_project, extract_form_info, object_project, object_grant, extract_form_info_grant, project_update
import socket
from sqlalchemy.exc import IntegrityError
from ..static.info import instructions 
import smtplib

projects = Blueprint('projects', __name__)

@projects.route("/project/new", methods=['GET', 'POST'])
@login_required
def new_project():
    form = ProjectForm()
    if form.validate_on_submit():
        #user = User.query.filter_by(email=form.email.data).first()
        user = current_user
        project = object_project(form)
        try:
            db.session.add(project)
            db.session.commit()
            dico = extract_form_info(form)
            #current_project = int(len(Project.query.all()))
            try:
                send_recap_project(user, body=dico, form= form, project_id=project.project_token) #user
                flash("Votre projet a été créé avec succès & Un email a été envoyé avec un récapitulatif de votre projet", 'info')
                return render_template('recapProject.html', title=project.project_title, form=form)
            except socket.gaierror:
                flash("Veuillez vérifier votre connexion réseau et réessayer", 'warning')
        #except AttributeError:
        #    flash('None type error (the mail should be the same as your mail in Account informations)', 'warning')
        #    return render_template('errors/errorPage.html', title='ERROR')
        except IntegrityError as e:
            flash(f"Un projet portant le même titre a déjà été envoyé à l'équipe de bioinformaticiens.",'warning')
    return render_template('create_project.html', title='Nouveau Projet', form=form, legend='Nouveau Projet', instructions=instructions('new_project'))

@projects.route("/project/<int:project_id>")
def project(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project.html', title=project.project_title, project=project)

@projects.route("/grant/<int:grant_id>")
def grant(grant_id):
    grant = Grant.query.get_or_404(grant_id)
    return render_template('grant.html', title=grant.project_title, grant=grant)

@projects.route("/project/<int:project_id>/update", methods=['GET', 'POST'])
@login_required
@admin_required
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    #---- before : only author can update | now : only admins can update
    #if project.author != current_user:
    #    abort(403)
    form = ProjectForm()
    if form.validate_on_submit():
        project_update(form, project, 'POST')
        flash("Votre projet a été mis à jour !", 'success')
        return redirect(url_for('projects.project', project_id=project.id))
    elif request.method == 'GET':
        project_update(form, project, 'GET')
    return render_template('create_project.html', title = 'Mise à jour du projet', form=form, legend = 'Mise à jour du projet')

@projects.route("/project/<int:project_id>/delete", methods=['POST'])
@login_required
@admin_required
def delete_projects(project_id):
    print('delete project =============================================')
    project = Project.query.get_or_404(project_id)
    proj_req = Project_request.query.get_or_404(project_id)
    #if project.author != current_user:
    #    abort(403)
    db.session.delete(project)
    db.session.delete(proj_req)
    db.session.commit()
    flash('Votre projet a été supprimé !', 'success')
    return redirect(url_for('main.project_home'))

##################33 GRANT
@projects.route("/grant/<int:grant_id>/update", methods=['GET', 'POST'])
@login_required
@admin_required
def update_grant(grant_id):
    grant = Grant.query.get_or_404(grant_id)
    #---- before : only author can update | now : only admins can update
    #if project.author != current_user:
    #    abort(403)
    form = GrantForm()
    if form.validate_on_submit():
        project_update(form, grant, 'POST')
        flash("Votre demande d'aide à une subvention a été mise à jour !", 'success')
        return redirect(url_for('projects.project', grant_id=grant.id))
    elif request.method == 'GET':
        project_update(form, grant, 'GET')
    return render_template('create_grant.html', title = "Mise à jour de l'aide financière", form=form, legend = "Mise à jour de l'aide financière")

@projects.route("/grant/<int:grant_id>/delete", methods=['POST'])
@login_required
@admin_required
def delete_grants(grant_id):
    grant = Grant.query.get_or_404(grant_id)
    proj_req = Project_request.query.get_or_404(grant_id)
    #if project.author != current_user:
    #    abort(403)
    db.session.delete(grant)
    db.session.delete(proj_req)
    db.session.commit()
    flash('Votre subvention a été supprimée !', 'success')
    return redirect(url_for('main.project_home'))

#######
    

@projects.route("/grant/new", methods=['GET', 'POST'])
@login_required
def new_grant():
    form = GrantForm()
    if form.validate_on_submit():
        #user = User.query.filter_by(email=form.email.data).first()
        user = current_user
        grant = object_grant(form)
        try:
            db.session.add(grant)
            db.session.commit()
            dico = extract_form_info_grant(form)
            try:
                send_recap_project(user, body=dico, form= form, project_id=grant.project_token)
                flash("Votre projet a été créé avec succès & Un email a été envoyé avec un récapitulatif de votre subvention.", 'info')
                return render_template('recapGrant.html', title=grant.project_title, form=form)
            except socket.gaierror:
                flash('Veuillez vérifier votre connexion réseau et réessayer', 'warning')
        except IntegrityError as e:
            flash(f"Une subvention de projet portant le même titre a déjà été envoyée à l'équipe de bioinformaticiens.",'warning')
    return render_template('create_grant.html', title='Nouvelle subvention', form=form, legend='Nouvelle subvention',instructions=instructions('new_project').replace('Projet', 'Grant'))
