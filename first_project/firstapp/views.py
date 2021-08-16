from django.shortcuts import HttpResponse, render
from django.utils import timezone
from .models import Task
import json
import os


def hello(request):
    return HttpResponse("""<h1><b><u><i><s>Hello World!</s></i></u></b></h1>""")


def home(request):
    return render(request, "firstapp/homepage.html")


def daytime(request):
    now = timezone.now()
    return HttpResponse(f"<h1>%s/%s</h1>" % (now.date(), now.time()))


def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, "firstapp/list_tasks.html", {"task_list": tasks})


def ret_dict_square(request):
    dct = {}
    for i in range(1, 16):
        dct[i] = i ** 2

    return HttpResponse(f"""<h1>%s</h1>""" % dct)


def bye(request):
    return HttpResponse(f"""<h1>bye<h1>""")


def rjson(request):
    with open(os.path.join(os.getcwd(), 'firstapp', 'read.json'), 'r') as f:
        j = json.load(f)
    return HttpResponse(f"""<h1>{j}</h1>""")


def lol(request):
    return HttpResponse(f"""<h1>LOL</h1>""")
