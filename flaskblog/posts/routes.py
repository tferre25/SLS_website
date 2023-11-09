from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm
from flaskblog.posts.utils import save_picture, send_post_email
from ..static.info import instructions

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        user = current_user
        if form.image_file.data:
            picture_file = save_picture(form.image_file.data)
            post = Post(title=form.title.data, content=form.content.data, image_file=picture_file,author=current_user)
        else:
            picture_file = None
            post = Post(title=form.title.data, content=form.content.data,author=current_user)
            #current_user.image_file = picture_file
        db.session.add(post)
        db.session.commit()
        flash(f'Votre post a été créé !', 'success')
        send_post_email(user)
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post', instructions=instructions('new_post'))


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update",  methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        picture_file = post.image_file #ancienne image
        if form.image_file.data:
            picture_file = save_picture(form.image_file.data)
            #current_user.image_file = picture_file
        post.title = form.title.data
        post.content = form.content.data
        post.image_file = picture_file
        db.session.commit()
        flash('Votre poste a été mis à jour !', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.image_file.data = post.image_file
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete",  methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Votre poste a été supprimé !', 'success')
    return redirect(url_for('main.home'))

