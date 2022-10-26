from email import contentmanager
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

# post model
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField()


