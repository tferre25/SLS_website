from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post, Comment, User
from flaskblog.posts.forms import PostForm, CommentForm
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

@posts.route("/post/<int:post_id>/add_comment",  methods=['GET', 'POST'])
@login_required
def comment(post_id):
    comments = Comment.query.all()
    user = current_user
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(post_title=post.title, content=form.comment.data, user_comment=user.username)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('comment_post.html', form=form, post=post, comments=comments, User=User)


@posts.route("/post/<int:post_id>/delete_comment",  methods=['POST'])
@login_required
def delete_comment(post_id):
    post = Post.query.get_or_404(post_id)
    comment = Comment.query.filter_by(post_title=post.title).first()
    if comment.user_comment != current_user.username:
        #flash(current_user, 'warning')
        abort(403)
    db.session.delete(comment)
    db.session.commit()
    flash('Votre commentaire a été supprimé !', 'success')
    return redirect(url_for('main.home'))