from django.contrib import admin
from .models import Project, Property, Ticket, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Ticket)
class TicketAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'ticket', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')


admin.site.register(Property)
admin.site.register(Project)