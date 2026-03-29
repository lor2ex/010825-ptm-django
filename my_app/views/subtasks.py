from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView

from my_app.models import SubTask
from my_app.serializers.subtask import SubTaskSerializer, SubTaskCreateSerializer




class SubTaskListCreateView(APIView, PageNumberPagination):
    page_size = 5

    def get(self, request: Request) -> Response:
        queryset = SubTask.objects.all().order_by('-created_at')

        task = request.query_params.get('task')
        status_param = request.query_params.get('status')
        if task:
            queryset = queryset.filter(task__title__iexact=task)
        if status_param:
            queryset = queryset.filter(status__iexact=status_param)

        results = self.paginate_queryset(
            queryset,
            request,
            view=self)

        serializer = SubTaskSerializer(results, many=True)

        return self.get_paginated_response(
            data=serializer.data,
        )

    def post(self, request: Request) -> Response:
        serializer = SubTaskCreateSerializer(
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


class SubTaskDetailUpdateDeleteView(APIView):
    def get_subtask(self, pk: int) -> SubTask:
        try:
            subtask = SubTask.objects.get(pk=pk)
        except SubTask.DoesNotExist:
            raise NotFound(f"Подзадача по ID - {pk} не найдена")
        return subtask

    def get(self, request, pk):
        subtask = self.get_subtask(pk)
        serializer = SubTaskSerializer(subtask)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        subtask = self.get_subtask(pk)
        serializer = SubTaskCreateSerializer(
            instance=subtask,
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
        subtask = self.get_subtask(pk)

        serializer = SubTaskCreateSerializer(
            instance=subtask,
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
        subtask = self.get_subtask(pk)
        subtask.delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)
