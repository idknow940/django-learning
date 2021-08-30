from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskCreateForm, TaskCreateCustomForm
from django.views.generic import View, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def get_home_page(request):
    tasks = Task.objects.filter(user_id=request.user.id)
    return render(request, 'tasks/home.html', {"tasks": tasks})


@login_required
class TaskView(View):
    template_name = 'tasks/home.html'

    def get(self, request):
        tasks = Task.objects.filter(user_id=self.request.user.id)
        return render(self.request, self.template_name, {"tasks": tasks})


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'

    # queryset = Task.objects.filter(user_id=self.request.user.id)
    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task

    def get_context_data(self, **kwargs):
        context = {
            'task_id': self.object.id,
            'task': self.object,
        }
        return context


class TaskCreateView(View):
    form = TaskCreateForm

    def get(self, request):
        form = self.form()
        context = {'form': form}
        return render(request, 'tasks/new_task.html', context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            form.save()
            return redirect('home')


class NewTaskCreateView(CreateView):
    form_class = TaskCreateForm
    model = Task
    template_name = 'tasks/new_task.html'
    success_url = '/'


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
        task = Task.objects.get(id=task_id, user_id=request.user.id)
    except Task.DoesNotExist:
        return redirect('home')
    form = TaskCreateForm(instance=task)
    if request.method == 'POST':
        form = TaskCreateForm(request.POST, instance=task)
        print(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task = form.save(commit=False)
            if request.FILES.get('image', None) is not None:
                task.image = request.FILES['image']
            task.save()
            return redirect('task_view', task_id)
    return render(request, 'tasks/task_update.html', {'form': form})
