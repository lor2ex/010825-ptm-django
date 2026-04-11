from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from my_app.models import SubTask
from my_app.serializers.subtask import SubTaskSerializer, SubTaskCreateSerializer, SubTaskUpdateSerializer


class SubTaskListCreateView(ListCreateAPIView):
    queryset = SubTask.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SubTaskCreateSerializer
        return SubTaskSerializer


class SubTaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return SubTaskUpdateSerializer
        return SubTaskSerializer






# class SubTaskListCreateView(APIView):
#     def get(self, request: Request) -> Response:
#         queryset = SubTask.objects.all()
#
#         serializer = SubTaskSerializer(queryset, many=True)
#
#         return Response(
#             data=serializer.data,
#             status=status.HTTP_200_OK
#         )
#
#     def post(self, request: Request) -> Response:
#         serializer = SubTaskCreateSerializer(
#             data=request.data
#         )
#         if not serializer.is_valid():
#             return Response(
#                 data=serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#         serializer.save()
#
#         return Response(
#             data=serializer.data,
#             status=status.HTTP_201_CREATED
#         )
#
#
# class SubTaskDetailUpdateDeleteView(APIView):
#     def get_subtask(self, pk: int) -> SubTask:
#         try:
#             subtask = SubTask.objects.get(pk=pk)
#         except SubTask.DoesNotExist:
#             raise NotFound(f"SubTask by ID - {pk} not found")
#         return subtask
#
#     def get(self, request, pk):
#         subtask = self.get_subtask(pk)
#         serializer = SubTaskSerializer(subtask)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
#     def put(self, request, pk):
#         subtask = self.get_subtask(pk)
#         serializer = SubTaskCreateSerializer(
#             instance=subtask,
#             data=request.data
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_200_OK
#             )
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )
#
#     def patch(self, request: Request, pk) -> Response:
#         subtask = self.get_subtask(pk)
#
#         serializer = SubTaskCreateSerializer(
#             instance=subtask,
#             data=request.data,
#             partial=True
#         )
#
#         if not serializer.is_valid():
#             return Response(
#                 data=serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         serializer.save()
#
#         return Response(
#             data=serializer.data,
#             status=status.HTTP_200_OK
#         )
#
#     def delete(self, request, pk):
#         subtask = self.get_subtask(pk)
#         subtask.delete()
#         return Response(data={}, status=status.HTTP_204_NO_CONTENT)