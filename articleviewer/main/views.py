from django.shortcuts import render, redirect
from django import forms
from .models import Article
from .forms import ArticleCreateForm


def home(request):
    try:
        articles = Article.objects.all()
    except Article.DoesNotExist:
        return redirect('home')
    return render(request, 'main/home.html', {'articles': articles})


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


def delete_article(request, task_id):
    try:
        article = Article.objects.get(id=task_id)
    except Article.DoesNotExist:
        return redirect('home')
    article.delete()
    return redirect('home')
