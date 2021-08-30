from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('tasks/<int:pk>', views.TaskDetailView.as_view(), name='task_view'),
    path('task_delete/<int:task_id>', views.delete_task, name='task_delete'),
    path('create_task/', views.NewTaskCreateView.as_view(), name='task_make'),
    path('update_task/<int:task_id>', views.update_task, name='task_update')
]
