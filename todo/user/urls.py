from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<int:user_id>/', views.get_profile, name='profile'),
    path('update_profile/<int:user_id>/', views.update_profile, name='update_profile'),
]
