from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt, admin_required
from flaskblog.models import User, Post, Project, Project_request, Grant
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm, ProjectRequestForm, ProjectProgressForm,
                                   RequestResetForm, ResetPasswordForm)
from flaskblog.users.utils import save_picture, send_reset_email, send_project_request
#from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask_mail import Message
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import socket, sys
from sqlalchemy.exc import IntegrityError
from ..static.info import instructions
import smtplib
from random import *

users = Blueprint('users', __name__)

#--------------------------------------------------- Account---------------------------------------------------------
@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data,
                    aphp_num=form.aphp_num.data,
                    status=form.status.data,
                    password=hashed_password)
        db.session.add(user)
        try:
            # ADD email validation
            db.session.commit()
            flash(f"Votre compte a été créé ! Vous pouvez maintenant vous connecter", 'success')
            return redirect(url_for('users.login'))
        except IntegrityError as e:
            flash(f'Le paramètre doit être unique','warning')
    return render_template('register.html', title='Register', form=form, instructions=instructions('register'))

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash("Connexion non réussie. Veuillez vérifier l'email et le mot de passe", 'danger')
    return render_template('login.html', title='Login', form=form, instructions=instructions('login'))

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.aphp_num = form.aphp_num.data
        current_user.status = form.status.data
        db.session.commit()
        flash("Votre compte a été mis à jour", 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
        form.aphp_num.data=current_user.aphp_num
        form.status.data=current_user.status
    image_file = url_for('static', filename='profile_pics/'+ current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form, instructions=instructions('account'))

@users.route("/user/posts/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=3)
    return render_template('user_posts.html', posts=posts, user=user)

@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        try:
            send_reset_email(user)
            flash("Un courriel a été envoyé avec les instructions pour réinitialiser votre mot de passe.", 'info')
        except socket.gaierror:
            flash("Veuillez vérifier votre connexion réseau et réessayer", 'warning')
        except smtplib.SMTPNotSupportedError:
            flash(f"votre mail \"{form.email.data}\" n'est pas un mail APHP", 'warning')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset_Password', form=form)

@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash("Il s'agit d'un jeton non valide ou expiré", 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f"Votre mot de passe a été mis à jour ! Vous pouvez maintenant vous connecter", 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset_Password', form=form)


#--------------------------------------------------- project_request---------------------------------------------------------
@users.route("/user/projects/<string:username>")
def user_projects(username):
    page = request.args.get('page', 1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    projects = Project.query.filter_by(author=user)\
        .order_by(Project.date_posted.desc())\
        .paginate(page=page, per_page=3)
    return render_template('user_projects.html', projects=projects, user=user)

@users.route("/user/<string:username>/grant")
def user_grants(username):
    page = request.args.get('page', 1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    grants = Grant.query.filter_by(author=user)\
        .order_by(Grant.date_posted.desc())\
        .paginate(page=page, per_page=3)
    return render_template('user_grants.html', grants=grants, user=user)

@users.route('/project_request', methods=['GET', 'POST'])
@login_required
@admin_required
def project_request():
    form = ProjectRequestForm()
    if form.validate_on_submit():
        try:
            request = Project_request(project_id=form.project_id.data,
                                    author=current_user,
                                    asking_for = form.asking_for.data,
                                    project_request = form.project_request.data,
                                    motif = form.motif.data)
            # UNIQUE REQUEST
            db.session.add(request)
            db.session.commit()
            if form.asking_for.data == 'Requiring bioinformatics support' and form.project_request.data == 'Accepted':
                project = Project.query.filter_by(project_token=form.project_id.data).first() # celui qui a fait la demande du projet
                project.is_accepted = True
                db.session.commit()
            elif form.asking_for.data == 'Funding' and form.project_request.data == 'Accepted':
                project = Grant.query.filter_by(project_token=form.project_id.data).first() # celui qui a fait la demande du projet
                project.is_accepted = True
                db.session.commit()
            elif form.asking_for.data == 'Funding' and form.project_request.data == 'Refused':
                project = Grant.query.filter_by(project_token=form.project_id.data).first() # celui qui a fait la demande du projet
            else:
                project = Project.query.filter_by(project_token=form.project_id.data).first() # celui qui a fait la demande du projet

            # INTERNET
            try:
                send_project_request(project, form, request)
                flash(f'Félicitations, votre réponse au projet intitulé "{project.project_title}" a été envoyé avec succès à son créateur "{project.username}" ', 'success')
            except socket.gaierror:
                flash('Veuillez vérifier votre connexion réseau et réessayer', 'warning')
        except AttributeError:
            flash("L'identifiant saisi ne correspond à aucun projet. Veuillez vérifier l'identifiant reçu dans votre adresse e-mail.", 'warning')
            db.session.delete(request)
            db.session.commit()
        except IntegrityError:
            flash('Déjà fait pour ce projet', 'warning')

    return render_template('project_request.html', legend='Project Request', form = form)


#--------------------------------------------------- profile--------(-------------------------------------------------
@users.route("/user/<string:username>/profile")
def user_profile(username):
    user = User.query.filter_by(username=username).first()
    posts = Post.query.all()
    total_user_posts = 0
    for p in posts:
        post_username = User.query.get(p.user_id).username
        if post_username == username:
            total_user_posts +=1
    no_accepted = int(len(Project.query.filter_by(author=user, is_accepted=True).all()))
    no_refused = int(len(Project.query.filter_by(author=user, is_accepted=False).all()))
    return render_template('profile.html', user=user, posts = posts, no_accepted=no_accepted, no_refused=no_refused, total_user_posts=int(total_user_posts), instructions=instructions('profile'))



@users.route("/user/project_progress", methods=['GET', 'POST'])
@login_required
@admin_required
def project_progress():
    form = ProjectProgressForm()
    try:
        project = Project.query.filter_by(project_token=form.project_id.data).first()
        if form.validate_on_submit():
            flash(f"{project.project_title}", 'success')
            project.progress = form.progress.data
            db.session.commit()
            return redirect(url_for('main.project_home'))
    except AttributeError:
        flash("Project did not exist ! try again")
    return render_template('project_progress.html', legend="Niveau de progression d'un projet", form=form)