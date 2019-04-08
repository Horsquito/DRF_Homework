from django.shortcuts import render
from rest_framework import viewsets
from .models import Performer, Task
from .serializers import PerformerSerializer, TaskSerializer
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
# Create your views here.

class PerformerView(viewsets.ModelViewSet):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
