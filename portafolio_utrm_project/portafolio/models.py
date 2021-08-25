from django.db import models
from django.db.models.base import Model

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image=models.ImageField(upload_to='portafolio/image')
    url=models.URLField(blank=True)
