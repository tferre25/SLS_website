from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt, admin_required
from flaskblog.models import User, Post, Project, Project_request, Grant
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm, ProjectRequestForm,
                                   RequestResetForm, ResetPasswordForm)
from flaskblog.users.utils import save_picture, send_reset_email, send_project_request
#from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask_mail import Message
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import socket, sys
from sqlalchemy.exc import IntegrityError

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
            db.session.commit()
            flash(f'Your account has benn created! You are now able to log in', 'success')
            return redirect(url_for('users.login'))
        except IntegrityError as e:
            flash(f'{str(e)} Parameter should be unique','warning')
    return render_template('register.html', title='Register', form=form)

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
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

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
        flash('Your account has been updated', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
        form.aphp_num.data=current_user.aphp_num
        form.status.data=current_user.status
    image_file = url_for('static', filename='profile_pics/'+ current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@users.route("/user/<string:username>")
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
            flash('An email has been sent with instructions to reset your password', 'info')
        except socket.gaierror:
            flash('Please check your network connection and try again.', 'warning')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset_Password', form=form)

@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'Your password has ben updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset_Password', form=form)


#--------------------------------------------------- project_request---------------------------------------------------------
@users.route("/user/<string:username>/")
def user_projects(username):
    page = request.args.get('page', 1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    projects = Project.query.filter_by(author=user)\
        .order_by(Project.date_posted.desc())\
        .paginate(page=page, per_page=3)
    return render_template('user_projects.html', projects=projects, user=user)

@users.route("/user/<string:username>/")
def user_grants(username):
    page = request.args.get('page', 1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    grants = Grant.query.filter_by(author=user)\
        .order_by(Grant.date_posted.desc())\
        .paginate(page=page, per_page=3)
    return render_template('user_grants.html', projects=grants, user=user)

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
                flash(f'Congrat, your answer to the project entitled "{project.project_title}" has been successfully sent to its creator "{project.username}" ', 'success')
            except socket.gaierror:
                flash('Please check your network connection and try again.', 'warning')
        except AttributeError:
            flash('The id entered does not correspond to any project. please double check the id received in your mailbox', 'warning')
            db.session.delete(request)
            db.session.commit()
        except IntegrityError:
            flash('Already done for this project', 'warning')

    return render_template('project_request.html', legend='Project Request', form = form)


#--------------------------------------------------- profile---------------------------------------------------------
@users.route("/user/<string:username>/profile")
@login_required
def user_profile(username):
    user = User.query.filter_by(username=username).first()
    posts = Post.query.all()
    no_accepted = int(len(Project.query.filter_by(author=user, is_accepted=True).all()))
    no_refused = int(len(Project.query.filter_by(author=user, is_accepted=False).all()))
    return render_template('profile.html', user=user, posts = posts, no_accepted=no_accepted, no_refused=no_refused)


