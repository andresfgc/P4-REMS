from django.shortcuts import render
from .models import Project, Property
# Create your views here.


def get_todo_list(request):
    properties = Property.objects.all()
    context = {
        'properties': properties
    }
    return render(request, 'todo/todo_list.html', context)
