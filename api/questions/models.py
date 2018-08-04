from django.contrib.auth.models import User
from django.db import models


class TimeStampedModel(models.Model):
  posted_at = models.DateTimeField(auto_now_add=True)
  last_edited = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class Comment(TimeStampedModel):
  body = models.CharField(max_length=256)

  user = models.ForeignKey(User, on_delete=models.CASCADE)  
  

class Answer(TimeStampedModel):
  body = models.TextField()

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  comments = models.ManyToManyField(Comment)
  

class Question(TimeStampedModel):
  title = models.CharField(max_length=128)
  body = models.TextField()

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  comments = models.ManyToManyField(Comment)  
