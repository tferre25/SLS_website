from flask import render_template, request, Blueprint, flash, url_for, redirect
from flaskblog.models import Post, User, Project
from flask_login import login_required, current_user
from flaskblog.main.forms import SearchForm
import sys,os
sys.path.append('../flaskblog')
from flaskblog.config import get_admins
import random
from flaskblog import db, bcrypt


main = Blueprint('main', __name__)

admin_list= get_admins()

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1,type=int)
    # grab those posts from database
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route("/project_home")
@login_required
def project_home():
    if current_user.email in admin_list:
        page = request.args.get('page', 1,type=int)
        # grab those projects from database
        projects = Project.query.order_by(Project.date_posted.desc()).paginate(page=page, per_page=5)
        return render_template('project_home.html', projects=projects)
    else:
        flash(f'''
                This page summarizes the projects created by the members of the APHP.
                It is reserved to the team of bioinformaticians of the Saint-Louis hospital.
                You can't access it.
            ''', 'danger')
        return redirect(url_for('main.about'))


@main.route("/about_us")
def about_us():
    return render_template('about_us.html', title='About')

@main.route("/about")
def about():
    return render_template('about.html', title='About')

#------------------------------------------------------------ DOC --------------------------------------------#
@main.route("/about_us/omics")
def omics():
    return render_template('docs/omics.html', title='OMICS')

@main.route("/about_us/log")
def log():
    return render_template('docs/log.html', title='LOG_DEV')

@main.route("/about_us/web")
def web():
    return render_template('docs/web.html', title='WEB_DEV')

@main.route("/about_us/db")
def database():
    return render_template('docs/db.html', title='DB_DEV')

@main.route("/about_us/code")
def code():
    return render_template('docs/code.html', title='CODE_DEV')


# pass stuff to navBar
@main.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

# create search function
@main.route("/search",  methods=['GET','POST'])
@login_required
def search():
    form = SearchForm()
    posts = Post.query
    if form.validate_on_submit():
        target = form.searched.data
        #Query the database
        posts = posts.filter(Post.content.like('%'+target+'%'))
        posts = posts.order_by(Post.title).all()
        return render_template('search.html', form=form, posts=posts)
    return render_template('about.html', title='Home', posts=posts)


#------------------------------------------------ GENERATE RANDOM DATA ROUTES ---------------------------------------------
@main.route('/generate_posts')
def generate_posts():
    for i in range(10):
        title = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=15)).upper()
        content = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5)).capitalize() for i in range(200)]
        content = ' '.join(content)
        user_id = int(random.choices(range(1,len(User.query.all())), k=1)[0])
        post = Post(title=title, content=content, user_id=user_id)
        db.session.add(post)
    db.session.commit()
    flash('10 posts was generated', 'info')
    return redirect(url_for('main.home'))

@main.route('/delete_posts')
def delete_posts():
    for post in Post.query.all():
        db.session.delete(post)
        db.session.commit()
    flash('Delete all posts', 'info')
    return render_template('about.html', title='About')

@main.route('/generate_users')
def generate_users():
    for i in range(10):
        username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10)).upper()
        email = f'{username}@blog.com'
        password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10)).upper()
        user = User(username=username, email=email, password=password)
        db.session.add(user)
    db.session.commit()
    flash('10 users was generated', 'info')
    return render_template('about.html', title='Home')

@main.route('/delete_project')
def delete_projects():
    for proj in Project.query.all():
        db.session.delete(proj)
        db.session.commit()
    flash('Delete all projects', 'info')
    return render_template('about.html', title='About')