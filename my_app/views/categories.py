from urllib.request import Request
from rest_framework import viewsets

from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from my_app.models import Category
from my_app.serializers import CategorySerializer



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_deleted=False)
    serializer_class = CategorySerializer


    @action(methods=['GET',], detail=False)
    def count_tasks(self, request: Request) -> Response:
        queryset = self.get_queryset().annotate(
            count_tasks=Count('tasks')
        )

        serializer = self.get_serializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
