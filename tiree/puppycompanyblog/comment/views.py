from flask import render_template,url_for,flash,request,redirect,Blueprint
from flask_login import current_user,login_required
from puppycompanyblog import db
from puppycompanyblog.models import User, Comment, BlogPost
from puppycompanyblog.comment.forms import CommentForm

come = Blueprint('come',__name__)

@come.route('/<int:post_id>/creat', methods=['GET','POST'])
@login_required
def create_comment(post_id):

    com = Comment.query.get_or_404(post_id)

    form = CommentForm()

    if form.validate_on_submit():

        come = Comment(text=form.text.data,post_id=current_user.id)

        db.session.add(come)
        db.session.commit()
        flash('blog post created!')
        return redirect(url_for('come.cum', post_id=com.id))

    return render_template("comment.html",form=form)

@come.route('/<int:post_id>/car')
@login_required
def cum(post_id):
    com = Comment.query.get_or_404(post_id)
    sor = com.query.all()
    return render_template('all_comment.html',com=com,sor=sor)
                            
