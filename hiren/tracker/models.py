from django.db import models
from taggit.managers import TaggableManager
# Create your models here.


class Hiren(models.Model):
    tag = TaggableManager()
    amount = models.FloatField()
    description = models.TextField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)