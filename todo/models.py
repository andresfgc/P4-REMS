from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.project_name


class Property(models.Model):
    property_status = models.TextChoices("property\
    _status", "Available Quoted Reserved Rejected Sold")
    property_number = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(blank=True, choices=property_status.choices, max_length=10)
    price = models.IntegerField(null=False, blank=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.property_number


STATUS = ((0, "Draft"), (1, "Published"))


class Ticket(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_tickets"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogticket_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
