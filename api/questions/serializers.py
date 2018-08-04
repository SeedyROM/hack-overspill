from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Answer, Comment, Question


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'first_name')

class CommentSerializer(serializers.ModelSerializer):
  user = UserSerializer()

  class Meta:
    model = Comment
    fields = ('id', 'body', 'user')

class AnswerSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True, read_only=True)
  user = UserSerializer()

  class Meta:
    model = Answer
    fields = ('id', 'body', 'comments', 'user', 'posted_at', 'last_edited')

class QuestionSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True, read_only=True)
  answers = AnswerSerializer(many=True, read_only=True)  
  user = UserSerializer()

  class Meta:
    model = Question
    fields = ('id', 'title', 'body', 'answers', 'comments', 'user', 'posted_at', 'last_edited')
