from django.db import models

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=50, null=False, blank=False)
    Adress = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.project_name


class Property(models.Model):
    PropertyStatus= models.TextChoices("PropertyStatus", "Available Quoted Reserved Rejected Sold")
    #Location = models.ForeignKey(Project, on_delete=models.CASCADE)
    property_number = models.CharField(max_length=50, null=False, blank=False)
    Status = models.CharField(blank=True, choices=PropertyStatus.choices, max_length=10)
    #Sold = models.BooleanField(null=False, blank=False, default=False)
    Price = models.IntegerField(null=False, blank=False)
    last_modified = models.DateField(auto_now=True)
    project_id=models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.property_number
