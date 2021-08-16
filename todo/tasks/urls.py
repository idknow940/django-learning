from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home_page, name='home'),
    path('tasks/<int:task_id>', views.get_task, name='task_view'),
    path('task_delete/<int:task_id>', views.delete_task, name='task_delete'),
    path('create_task/', views.create_task, name='task_make'),
    path('update_task/<int:task_id>', views.update_task, name='task_update')
]
