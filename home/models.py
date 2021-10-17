from datetime import datetime
from django import contrib
from django.db import models
from django.db.models.base import Model
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
