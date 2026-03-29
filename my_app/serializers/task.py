from datetime import datetime

from rest_framework import serializers
from my_app.models import Task
from .subtask import SubTaskSerializer


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'deadline',
            'created_at',
        ]


class TasksCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "status",
            "deadline",
        ]

    def validate_deadline(self, value: datetime):
        if value < datetime.now():
            raise serializers.ValidationError(f"Дедлайн не может быть в прошлом")
        return value


class TasksUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskDetailSerializer(serializers.ModelSerializer):
    SubTask = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = "__all__"