from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# Create your models here.


class Hiren(models.Model):
    user = models.ForeignKey(User)
    tag = TaggableManager()
    amount = models.FloatField()
    description = models.TextField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)