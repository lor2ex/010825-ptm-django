from datetime import datetime

from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.db.models import Count
from rest_framework.views import APIView

from my_app.models import Task
from my_app.serializers.task import TasksSerializer, TasksCreateSerializer


class TaskListCreateView(APIView):
    WEEKDAYS = {
        'понедельник': 1,
        'вторник': 2,
        'среда': 3,
        'четверг': 4,
        'пятница': 5,
        'суббота': 6,
        'воскресенье': 7,
    }

    def get(self, request: Request) -> Response:
        queryset = Task.objects.all()

        day = request.query_params.get('day')
        if day:
            weekday = self.WEEKDAYS.get(day.strip().lower())
            if weekday:
                queryset = queryset.filter(deadline__iso_week_day=weekday)
            else:
                return Response(
                    data={"error": f"Неизвестный день недели: '{day}'"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer = TasksSerializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def get_page_size(self, request):
        page_size = request.query_params.get('page_size')
        if page_size and page_size.isdigit():
            return int(page_size)
        return self.page_size

    def post(self, request: Request) -> Response:
        serializer = TasksCreateSerializer(
            data=request.data
        )
        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )


class TaskDetailUpdateDeleteView(APIView):
    def get_object(self, pk: int) -> Task:
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise NotFound(f"Задача по ID - {pk} не найдена")
        return task

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TasksSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TasksCreateSerializer(
            instance=task,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request: Request, pk) -> Response:
        task = self.get_object(pk)

        serializer = TasksCreateSerializer(
            instance=task,
            data=request.data,
            partial=True
        )

        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)