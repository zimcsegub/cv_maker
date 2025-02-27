from django.db import models
from django.contrib.auth.models import User

class CV(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    summary = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    projects = models.TextField()
    certifications = models.TextField()

    def __str__(self):
        return self.full_name

# Create your models here.
