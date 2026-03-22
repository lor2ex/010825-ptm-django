from rest_framework import serializers

from my_app.models import Task


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


class TasksUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
