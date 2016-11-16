from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        pass

    def popular(self):
        pass

class Question(models.Model):
    title = models.CharField(max_length=70)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(to=User)
    likes = models.ManyToManyField(to=User)
    objects = QuestionManager

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(to=Question)
    author = models.ForeignKey(to=User)

