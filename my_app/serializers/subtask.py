from rest_framework import serializers
from my_app.models import SubTask



class SubTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubTask
        fields = [
            'id',
            'title',
            'description',
            'deadline',
            'created_at',
        ]


class SubTaskCreateSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(
        allow_null=True,
        required=False,
        style={"input_type": "text"},
    )
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = SubTask
        fields = "__all__"
        # extra_kwargs = {
        #     "created_at": {
        #         "read_only": True
        #     }
        # }


class SubTaskUpdateSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(
        allow_null=True,
        required=False,
        style={"input_type": "text"},
    )

    class Meta:
        model = SubTask
        fields = "__all__"