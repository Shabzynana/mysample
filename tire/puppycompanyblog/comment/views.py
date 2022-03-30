from flask import render_template,url_for,flash,request,redirect,Blueprint
from flask_login import current_user,login_required
from puppycompanyblog import db
from puppycompanyblog.models import User, Comment, BlogPost
from puppycompanyblog.comment.forms import CommentForm

come = Blueprint('come',__name__)


@come.route("/post/<int:post_id>/comment", methods=["GET", "POST"])
@login_required
def comment_post(post_id):


    post = BlogPost.query.get_or_404(post_id)
    imm = Comment.query.filter_by(post_id=post.id)

    #imm = Comment.query.all()

    form = CommentForm()

    #if request.method == 'POST': # this only gets executed when the form is submitted and not when the page loads
    if form.validate_on_submit():
        comment = Comment(text=form.text.data, post_id=post.id, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash("Your comment has been added to the post", "success")
        return redirect(url_for("come.comment_post", post_id=post.id))
    return render_template("comment.html", form=form, post_id=post_id,imm=imm,post=post)
