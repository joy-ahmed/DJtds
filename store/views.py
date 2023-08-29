from django.shortcuts import render

from store.models import TaskList

# Create your views here.


def store(request):
    all_tasks = TaskList.objects.all

    return render(request, "store.html", {"all_tasks": all_tasks})
