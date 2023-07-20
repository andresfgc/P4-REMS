from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Project, Property, Ticket, Comment
from .forms import PropertyForm, ProjectForm, CommentForm, TicketForm
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


# for Tickets.
class TicketList(generic.ListView):
    model = Ticket
    queryset = Ticket.objects.filter(status=1).order_by('-created_on')
    template_name = 'tickets.html'
    paginate_by = 6


    def add_ticket(request):
        if request.method == 'POST':
            form = TicketForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('tickets')
        form = TicketForm()
        context = {
            'form': form
        }
        return render(request, 'add_ticket.html', context)


    def edit_ticket(request, slug):
        ticket = get_object_or_404(Ticket, slug=slug)
        if request.method == 'POST':
            form = TicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                return redirect('tickets')
        form = TicketForm(instance=ticket)
        context = {
            'form': form
        }
        return render(request, 'edit_ticket.html', context)

    
    def delete_ticket(request, slug):
        ticket = get_object_or_404(Ticket, slug=slug)
        ticket.delete()
        return redirect('tickets')


class TicketDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Ticket.objects.filter(status=1)
        ticket = get_object_or_404(queryset, slug=slug)
        comments = ticket.comments.order_by('created_on')
        liked = False
        if ticket.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "ticket_detail.html",
            {
                "ticket": ticket,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Ticket.objects.filter(status=1)
        ticket = get_object_or_404(queryset, slug=slug)
        comments = ticket.comments.order_by('created_on')
        liked = False
        if ticket.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.ticket = ticket
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "ticket_detail.html",
            {
                "ticket": ticket,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class TicketLike(View):

    def post(self, request, slug):
        ticket = get_object_or_404(Ticket, slug=slug)

        if ticket.likes.filter(id=request.user.id).exists():
            ticket.likes.remove(request.user)
        else:
            ticket.likes.add(request.user)

        return HttpResponseRedirect(reverse('ticket_detail', args=[slug]))


# homepage
def homepage(request):
    return render(request, 'index.html')