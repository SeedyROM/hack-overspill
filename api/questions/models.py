from django.contrib.auth.models import User
from django.db import models


class TimeStampedModel(models.Model):
  posted_at = models.DateTimeField(auto_now_add=True)
  last_edited = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class Comment(TimeStampedModel):
  body = models.CharField(max_length=256)

  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  

  def __str__(self):
    return f'{self.user.username}: {self.body[:40]}...'
  

class Answer(TimeStampedModel):
  body = models.TextField()

  question = models.ForeignKey('questions.Question', on_delete=models.CASCADE, related_name='answers')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
  comments = models.ManyToManyField(Comment, blank=True)
  
  def __str__(self):
    return f'{self.question.title}: {self.body[:40]}...'

class Question(TimeStampedModel):
  title = models.CharField(max_length=128)
  body = models.TextField()

  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
  comments = models.ManyToManyField(Comment, blank=True)
  
  def __str__(self):
    return f'{self.title}: {self.user.username}'
