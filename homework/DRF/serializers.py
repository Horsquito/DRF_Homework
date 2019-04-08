from rest_framework import serializers
from .models import Performer, Task

class PerformerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Performer
        fields = ('id', 'url', 'name', 'email', 'task')

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'url', 'title', 'body', 'status')
