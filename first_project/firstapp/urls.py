from django.urls import path
from firstapp import views

urlpatterns = [
    path('hello/', views.hello),
    path('datetime/', views.daytime),
    path('list_task', views.list_tasks),
    path('', views.my_name),
]
