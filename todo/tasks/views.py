from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskCreateForm, TaskCreateCustomForm


@login_required
def get_home_page(request):
    tasks = Task.objects.filter(user_id=request.user.id)
    return render(request, 'tasks/home.html', {"tasks": tasks})


@login_required
def get_task(request, task_id):
    try:
        task_obj = Task.objects.get(id=task_id, user_id=request.user.id)
    except Task.DoesNotExist:
        return redirect("home")
    context = {
        "task_id": task_id,
        "task": task_obj
    }
    return render(request, 'tasks/task_view.html', context)


@login_required
def delete_task(request, task_id):
    try:
        task_obj = Task.objects.get(id=task_id, user_id=request.user.id)
    except Task.DoesNotExist:
        return redirect("home")
    task_obj.delete()
    return redirect('home')


@login_required
def create_task(request):
    form = TaskCreateForm()
    if request.method == 'POST':
        print(request.POST)
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'tasks/new_task.html', context)


@login_required
def create_c_task(request):
    form = TaskCreateCustomForm()
    if request.method == 'POST':
        print(request.POST)
        form = TaskCreateCustomForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Task.objects.create(**data)
            return redirect('home')
    context = {'form': form}
    return render(request, 'tasks/new_task.html', context)


@login_required
def update_task(request, task_id):
    try:
        task_obj = Task.objects.get(id=task_id, user_id=request.user.id)
    except Task.DoesNotExist:
        return redirect('home')
    form = TaskCreateForm(instance=task_obj)
    if request.method == 'POST':
        form = TaskCreateForm(request.POST, instance=task_obj)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_view', task_id=task_id)
    return render(request, 'tasks/task_update.html', {'form': form})
