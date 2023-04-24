from flask import render_template, request, Blueprint, flash, url_for, redirect
from flaskblog.models import Post, User, Project
from flask_login import login_required
from flaskblog.main.forms import SearchForm


main = Blueprint('main', __name__)



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
    page = request.args.get('page', 1,type=int)
    # grab those projects from database
    #projects = Project.query.all()
    projects = Project.query.order_by(Project.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('project_home.html', projects=projects)

@main.route("/about_us")
def about_us():
    return render_template('about_us.html', title='About')
    


@main.route("/about")
def about():
    return render_template('about.html', title='About')


# DOC
@main.route("/omics")
def omics():
    return render_template('docs/omics.html', title='OMICS')

@main.route("/log")
def log():
    return render_template('docs/log.html', title='LOG_DEV')

@main.route("/web")
def web():
    return render_template('docs/web.html', title='WEB_DEV')

@main.route("/db")
def db():
    return render_template('docs/db.html', title='DB_DEV')

@main.route("/code")
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