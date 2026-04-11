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


def validate_deadline(value: datetime):
    if value < datetime.now():
        raise serializers.ValidationError(f"Дедлайн не может быть в прошлом")
    return value


class TasksCreateSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(
        allow_null=True,
        required=False,
        style={"input_type": "text"},
    )

    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "status",
            "deadline",
        ]


class TasksUpdateSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(
        allow_null=True,
        required=False,
        style={"input_type": "text"},
    )

    class Meta:
        model = Task
        fields = "__all__"


class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
