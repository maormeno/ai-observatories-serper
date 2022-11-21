from django.db import models

# Create your models here.
class Link(models.Model):
    source = models.CharField(max_length=2048, unique=True)
    title = models.CharField(max_length=2048)
    country = models.CharField(max_length=256)
    keyword1 = models.CharField(max_length=256)
    keyword2 = models.CharField(max_length=256)
    created_at = models.DateField(default=None)
    updated_at = models.DateTimeField(null=True)
    label = models.CharField(max_length=64)
