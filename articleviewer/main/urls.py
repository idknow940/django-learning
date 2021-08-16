from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('create-article/', views.create_article, name='create-a'),
    path('delete-article/<int:task_id>', views.delete_article, name='delete-a')
]
