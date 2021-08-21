from django.shortcuts import render, redirect
from django import forms
from .models import Article, Comment
from .forms import ArticleCreateForm, CommentCreateForm


def home(request):
    try:
        articles = Article.objects.all()
        comments = Comment.objects.all()
    except Article.DoesNotExist:
        return redirect('home')
    return render(request, 'main/home.html', {'articles': articles, 'comments': comments})


def create_article(request):
    form = ArticleCreateForm()
    if request.method == 'POST':
        print(request.POST)
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'main/createarticle.html', context)


def delete_article(request, art_id):
    try:
        article = Article.objects.get(id=art_id)
    except Article.DoesNotExist:
        return redirect('home')
    article.delete()
    return redirect('home')


def delete_comment(request, c_id):
    try:
        comment = Comment.objects.get(id=c_id)
    except Comment.DoesNotExist:
        return redirect('home')
    comment.delete()
    return redirect('home')


def comment_article(request, art_id):
    try:
        article = Article.objects.get(id=art_id)
    except Article.DoesNotExist:
        return redirect('home')
    form = CommentCreateForm()
    if request.method == 'POST':
        print(request.POST)
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'main/createcomment.html', context)
