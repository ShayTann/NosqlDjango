from django.db import models
from django.contrib.auth.models import UserManager
import datetime
# Create your models here.

class Topic(models.Model):
    author = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    number_comments = models.IntegerField(default="0")
    body = models.CharField(max_length=255,default="")
    score = models.CharField(max_length=255)
    subreddit = models.CharField(max_length=255,default="")
    positivity = models.IntegerField(default="0")
    negativity = models.IntegerField(default="0")
    clustering1 = models.TextField(default="")
    clustering2 = models.TextField(default="")
    objects = UserManager()
    def __str__(self):
        return self.body



class Comment(models.Model):
    author = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    body = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)

class SupportEvolution(models.Model):
    hour = models.CharField(max_length=255,default="0")
    positivity = models.IntegerField(default="0")
    negativity = models.IntegerField(default="0")
