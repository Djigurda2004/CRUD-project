from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from arts.models import Articles
from .models import Comment
from django.http import HttpResponseForbidden

@login_required
def add_comment(request,article_id):
    article = get_object_or_404(Articles,id=article_id)
    if request.method == "POST":
        text = request.POST.get("text")
        parent_id = request.POST.get("parent")
        parent = Comment.objects.get(id=parent_id) if parent_id else None
        comment = Comment.objects.create(article=article,author=request.user,text=text,parent=parent)
        if request.headers.get('HX-Request'):
            return render(request, 'comments/comments.html', {'node': comment})
    return redirect('arts:detail',article.id)

@login_required
def delete_comment(request,comment_id):
    comment = get_object_or_404(Comment,id=comment_id)
    if request.user == comment.author:
        article_id = comment.article.id
        comment.delete()
    return redirect('arts:detail',article_id)

@login_required
def update_comment(request,comment_id):
    comment =  get_object_or_404(Comment,id=comment_id)
    if request.user != comment.author:
        return HttpResponseForbidden()
    if request.method == "POST":
        comment.text = request.POST.get("text")
        comment.save()
        return redirect('arts:detail',comment.article.id)
    return render(request, "comments/add_comment.html", {"comment": comment})

@login_required
def like_comment(request,comment_id):
    comment = get_object_or_404(Comment,id = comment_id)
    if request.user not in comment.likes.all():
        comment.likes.add(request.user)
    else:
        comment.likes.remove(request.user)
    return redirect('arts:detail',comment.article.id)