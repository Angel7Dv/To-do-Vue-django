from django.shortcuts import render

# Create your views here.
from .models import Task
from .serializers import TaskSerializer

from rest_framework import viewsets

#para la autentificacion


class TaskViewSet(viewsets.ModelViewSet):

    #solo esto es necesario
    queryset = Task.objects.all()
    serializer_class = TaskSerializer