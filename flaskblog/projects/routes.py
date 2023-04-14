from flask import Blueprint
from flask import render_template, flash, Blueprint
from flaskblog.projects.forms import ProjectForm, GrantForm

projects = Blueprint('projects', __name__)

@projects.route("/project", methods=['GET', 'POST'])
def project():
    form = ProjectForm()
    if form.validate_on_submit():
        flash(f'Project {form.project_title.data} was created and has been sent in your email adress!', 'success')
        return render_template('recapProject.html', title='project', form=form)
    return render_template('project.html', title='project', form=form)

@projects.route("/grant", methods=['GET', 'POST'])
def grant():
    form = GrantForm()
    if form.validate_on_submit():
        flash(f'writing assistance {form.projectTitle.data} was created!', 'success')
        return render_template('recapGrant.html', title='grant', form=form)
    return render_template('grant.html', title='grant', form=form)