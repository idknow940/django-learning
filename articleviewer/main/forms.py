from django import forms
from .models import Article, Comment


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
