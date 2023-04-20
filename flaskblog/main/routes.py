from flask import render_template, request, Blueprint, flash, url_for, redirect
from flaskblog.models import Post
from flask_login import login_required


main = Blueprint('main', __name__)



@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1,type=int)
    # grab those posts from database
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

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
