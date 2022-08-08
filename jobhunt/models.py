from django.db import models


# MALE = "Erkak"
STANDART = "Standart"
URGENT = "Urgent"
PREMIUM = "Premium"
JOB_STATUS_CHOICE = (
    (STANDART, "Standart"),
    (PREMIUM, "Premium"),
    (URGENT, "Urgent")
)

class  Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    

class Employer(models.Model):
    pass

class Location(models.Model):
    title = models.CharField(max_length=256)
    slug =  models.SlugField()
    

class Job(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to="images/")
    price_from = models.IntegerField(default=0)
    price_to = models.IntegerField(default=0)
    status = models.CharField(max_length=4096, choices=JOB_STATUS_CHOICE)
    
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    employer = models.ForeignKey("Employer", on_delete=models.CASCADE)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)

    created_at = models.DateField()
    updated_at = models.DateField()