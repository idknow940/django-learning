from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskCreateForm, TaskCreateCustomForm


def get_home_page(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/home.html', {"tasks": tasks})


def get_task(request, task_id):
    try:
        task_obj = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return redirect("home")
    context = {
        "task_id": task_id,
        "task": task_obj
    }
    return render(request, 'tasks/task_view.html', context)


def delete_task(request, task_id):
    try:
        task_obj = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return redirect("home")
    # TODO implement message when successfully deleting the task.
    task_obj.delete()
    return redirect('home')


def create_task(request):
    form = TaskCreateForm()
    if request.method == 'POST':
        print(request.POST)
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'tasks/new_task.html', context)


def create_c_task(request):
    form = TaskCreateCustomForm()
    if request.method == 'POST':
        print(request.POST)
        form = TaskCreateCustomForm(request.POST)
        if form.is_valid():
            # TODO ADD SAVE
            data = form.cleaned_data
            Task.objects.create(**data)
            return redirect('home')
    context = {'form': form}
    return render(request, 'tasks/new_task.html', context)


def update_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    context = {
        "task_id": task_id,
        "task": task_obj,
    }
    return render(request, 'tasks/task_update.html', context)
