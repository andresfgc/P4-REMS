from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Project, Property, Post
from .forms import PropertyForm, ProjectForm
# Create your views here.


# for properties.
def get_properties(request):
    properties = Property.objects.all()
    context = {
        'properties': properties
    }
    return render(request, 'properties.html', context)


def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('properties')
    form = PropertyForm()
    context = {
        'form': form
    }
    return render(request, 'add_property.html', context)


def edit_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('properties')
    form = PropertyForm(instance=property)
    context = {
        'form': form
    }
    return render(request, 'edit_property.html', context)


def delete_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    property.delete()
    return redirect('properties')

# for projects.
def get_projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    form = ProjectForm()
    context = {
        'form': form
    }
    return render(request, 'add_project.html', context)


def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    form = ProjectForm(instance=project)
    context = {
        'form': form
    }
    return render(request, 'edit_project.html', context)


def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('projects')


# for Posts.
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )