from django import forms
from .models import Property, Project


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['property_number', 'Price', 'Status', 'project']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'Adress']