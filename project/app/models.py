from django.db import models

# Create your models here.
class Link(models.Model):
    source = models.CharField(max_length=2048)
    title = models.CharField(max_length=2048)
    country = models.CharField(max_length=256)
    keyword1 = models.CharField(max_length=256)
    keyword2 = models.CharField(max_length=256)
    label = models.CharField(max_length=64)
    
    