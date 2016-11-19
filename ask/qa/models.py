from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')[0:10]

    def popular(self):
        return self.order_by('rating')

class Question(models.Model):
    title = models.CharField(max_length=70)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(to=User)
    likes = models.ManyToManyField(to=User, related_name='question_like_user')
# through='Likes')
    objects = QuestionManager()

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User)

#class Likes(model.Model):
#    user_id = models.ForeignKey(to=User, related_name='like_user')
#    question_id = model.ForeignKey(to=Question,related_name='like_question')