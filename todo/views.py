from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Property
from .forms import PropertyForm
# Create your views here.


def get_todo_list(request):
    properties = Property.objects.all()
    context = {
        'properties': properties
    }
    return render(request, 'todo/todo_list.html', context)


def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = PropertyForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_property.html', context)


def edit_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = PropertyForm(instance=property)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_property.html', context)


def toggle_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    property.Price = not property.Price
    property.Status = not property.Status
    property.save()
    return redirect('get_todo_list')


def delete_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    property.delete()
    return redirect('get_todo_list')