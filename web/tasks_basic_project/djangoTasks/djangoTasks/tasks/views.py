from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from djangoTasks.tasks.models import Task


def show_bare_minimum(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


def get_all_tasks(request):
    all_tasks = Task\
        .objects\
        .order_by('id')\
        .all()
    result = ', '.join(f'{t.task_name}({t.id})' for t in all_tasks)
    print(result)
    return HttpResponse(result)


def index(request):
    all_tasks = Task \
        .objects \
        .order_by('id') \
        .all()
    context = {
        'title': 'The tasks app!',
        'tasks': all_tasks
    }
    print(all_tasks)
    return render(request, 'index.html', context)
