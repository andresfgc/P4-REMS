from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('accounts', include('allauth.urls')),
]


