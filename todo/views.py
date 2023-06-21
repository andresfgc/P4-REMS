from django.shortcuts import render, redirect
from .models import Project, Property
# Create your views here.


def get_todo_list(request):
    properties = Property.objects.all()
    context = {
        'properties': properties
    }
    return render(request, 'todo/todo_list.html', context)


def add_property(request):
    if request.method == 'POST':
        property_number = request.POST.get('property_number')
        Status = request.POST.get('Status')
        Price = request.POST.get('Price')
        #  done = 'done' in request.POST
        Property.objects.create(property_number=property_number, Status=Status, Price=Price)

        return redirect('get_todo_list')
    return render(request, 'todo/add_property.html')