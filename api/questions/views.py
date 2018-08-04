from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import Response

from .models import Question
from .serializers import QuestionSerializer


@api_view(['GET'])
def get_question(request, pk):
  question = get_object_or_404(Question, pk=pk)
  json = QuestionSerializer(question)

  return Response(json.data)