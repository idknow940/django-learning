from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('create-article/', views.create_article, name='create-a'),
    path('delete-article/<int:art_id>', views.delete_article, name='delete-a'),
    path('delete-comment/<int:c_id>', views.delete_comment, name="delete-c"),
    path('comment-article/<int:art_id>', views.comment_article, name='comment-a'),
]
