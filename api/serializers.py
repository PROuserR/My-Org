from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'