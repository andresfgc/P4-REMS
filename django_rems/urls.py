"""django_rems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('tickets', views.TicketList.as_view(), name='tickets'),
    path('add_ticket', views.TicketList.add_ticket, name='add_ticket'),
    path('edit_ticket/<slug:slug>', views.TicketList.edit_ticket, name='edit_ticket'),
    path('delete_ticket/<slug:slug>', views.TicketList.delete_ticket, name='delete_ticket'),
    path('like/<slug:slug>', views.TicketLike.as_view(), name='ticket_like'),
    path("accounts/", include("allauth.urls")),
    path('properties', views.get_properties, name='properties'),
    path('add', views.add_property, name='add'),
    path('edit/<property_id>', views.edit_property, name='edit'),
    path('delete/<property_id>', views.delete_property, name='delete'),
    path('projects', views.get_projects, name='projects'),
    path('add_project', views.add_project, name='add_project'),
    path('edit_project/<project_id>', views.edit_project, name='edit_project'),
    path('delete_project/<project_id>', views.delete_project, name='delete_project'),
    path('summernote', include('django_summernote.urls')),
    path('<slug:slug>/', views.TicketDetail.as_view(), name='ticket_detail'),
]
