from django.shortcuts import HttpResponse
from django.utils import timezone
from .models import Task


def hello(request):
    return HttpResponse("""<h1><b><u><i><s>Hello World!</s></i></u></b></h1>""")


def my_name(request):
    return HttpResponse(
        """"<h1><u><i>My name is Alek Aleksanyan</i></u></h1>""")


def daytime(request):
    now = timezone.now()
    return HttpResponse(f"<h1>%s/%s</h1>" % (now.date(), now))


def list_tasks(request):
    tasks = Task.objects.all()
    html = f"""
    <h2>tasks</h2>
    <h3>tasks: {tasks[0]}</h3>
    <h3>tasks: {tasks[1]}</32>
    """
    return HttpResponse(html)
