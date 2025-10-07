from django.shortcuts import render, HttpResponse
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()

    for task in tasks:
        task.completed = not task.completed
        task.save()
    return render(request, 'index.html', context={'tasks':tasks})
