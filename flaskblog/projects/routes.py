from flask import Blueprint, redirect, url_for, abort, request
from flask import render_template, flash, Blueprint
from flaskblog.projects.forms import ProjectForm, GrantForm
from flask_login import login_required, current_user
from flaskblog.models import User, Project, Grant
from flaskblog import db, admin_required
from flaskblog.projects.utils import send_recap_project, extract_form_info, object_project, object_grant, extract_form_info_grant, project_update

projects = Blueprint('projects', __name__)

@projects.route("/project/new", methods=['GET', 'POST'])
@login_required
def new_project():
    form = ProjectForm()
    #try:
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        project = object_project(form)
        db.session.add(project)
        db.session.commit()
        dico = extract_form_info(form)
        current_project = int(len(Project.query.all()))
        send_recap_project(user, body=dico, form= form, project_id=current_project)
        flash('Your project hes been created succesfully & An email has been sent with a recap of your project', 'info')
        return render_template('recapProject.html', title='Project', form=form)
    #except AttributeError:
    #    flash('None type error (the mail should be the same as your mail in Account informations)', 'warning')
    #    return render_template('errors/errorPage.html', title='ERROR')
    return render_template('create_project.html', title='New Project', form=form, legend='New Project')

@projects.route("/project/<int:project_id>")
def project(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project.html', title=project.project_title, project=project)

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
        flash('Your project had been updated !', 'success')
        return redirect(url_for('projects.project', project_id=project.id))
    elif request.method == 'GET':
        project_update(form, project, 'GET')
    return render_template('create_project.html', title = 'Update Project', form=form, legend = 'Update Project')

@projects.route("/project/<int:project_id>/delete", methods=['POST'])
@login_required
@admin_required
def delete_projects(project_id):
    project = Project.query.get_or_404(project_id)
    #if project.author != current_user:
    #    abort(403)
    db.session.delete(project)
    db.session.commit()
    flash('Your project had been deleted !', 'success')
    return redirect(url_for('main.project_home'))
    

@projects.route("/grant/new", methods=['GET', 'POST'])
@login_required
def new_grant():
    form = GrantForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        grant = object_grant(form)
        db.session.add(grant)
        db.session.commit()
        dico = extract_form_info_grant(form)
        send_recap_project(user, body=dico, form= form)
        flash(f'writing assistance {form.project_title.data} was created!', 'success')
        return render_template('recapGrant.html', title='grant', form=form)
    return render_template('grant.html', title='grant', form=form)


