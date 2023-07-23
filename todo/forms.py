from django import forms
from .models import Property, Project, Comment, Ticket


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['property_number', 'price', 'status', 'project']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'address']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['property', 'title', 'slug', 'author', 'featured\
        _image', 'excerpt', 'content', 'status']
