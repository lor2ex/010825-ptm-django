from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView

from my_app.models import SubTask
from my_app.serializers.subtask import SubTaskSerializer, SubTaskCreateSerializer




class SubTaskListCreateView(APIView):
    def get(self, request: Request) -> Response:
        queryset = SubTask.objects.all()

        serializer = SubTaskSerializer(queryset, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
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
            raise NotFound(f"SubTask by ID - {pk} not found")
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