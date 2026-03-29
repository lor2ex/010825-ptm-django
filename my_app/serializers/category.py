from rest_framework import serializers
from my_app.models import Category



error_txt = "Категория уже существует"

class CategorySerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        if self.instance:  # update
            if Category.objects.filter(name=value).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError(error_txt)
        else:  # create
            if Category.objects.filter(name=value).exists():
                raise serializers.ValidationError(error_txt)
        return value

    class Meta:
        model = Category
        fields = "__all__"





# class CategoryCreateSerializer(serializers.ModelSerializer):
#     def create(self, validated_data):
#         if Category.objects.filter(name=validated_data['name']).exists():
#             raise serializers.ValidationError("Категория с таким названием уже существует")
#         return super().create(validated_data)
#
#     class Meta:
#         model = Category
#         fields = "__all__"
#
#
#
# class CategoryUpdateSerializer(serializers.ModelSerializer):
#     def update(self, instance, validated_data):
#         if Category.objects.filter(name=validated_data['name']).exclude(id=instance.id).exists():
#             raise serializers.ValidationError("Категория с таким названием уже существует")
#         return super().update(instance, validated_data)
#
#     class Meta:
#         model = Category
#         fields = "__all__"