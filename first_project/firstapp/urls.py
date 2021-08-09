from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.my_name),
    path('hello/', views.hello),
    path('datetime/', views.daytime),
    path('list_task/', views.list_tasks),
    path('dict/', views.ret_dict_square),
    path('bye/', views.bye),
    path('json/', views.rjson),
    path('lol/', views.lol),
]
