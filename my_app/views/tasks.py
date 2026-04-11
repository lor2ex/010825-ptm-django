from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from my_app.models import Task
from my_app.serializers.task import TasksSerializer, TasksCreateSerializer, TasksUpdateSerializer



class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()

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
            return TasksCreateSerializer
        return TasksSerializer


class TaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return TasksUpdateSerializer
        return TasksSerializer







# @api_view(['GET'])
# def get_all_tasks(request: Request) -> Response:
#     queryset = Task.objects.all()
#     serializer = TasksSerializer(queryset, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET'])
# def get_task_by_id(request: Request, pk: int) -> Response:
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return Response(
#             {"error": f"Task with ID {pk} does not exist"},
#             status=status.HTTP_404_NOT_FOUND,
#         )
#     serializer = TasksSerializer(task)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['POST'])
# def create_new_task(request: Request) -> Response:
#         serializer = TasksCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(
#             data=serializer.data,
#             status=status.HTTP_201_CREATED
#         )
#
#
# @api_view(['GET'])
# def get_tasks_statistic(request: Request) -> Response:
#     total = Task.objects.count()
#     by_status = Task.objects.values('status').annotate(count=Count('id'))
#     overdue = Task.objects.filter(deadline__lt=timezone.now()).count()
#
#     return Response(
#         data={
#             "total": total,
#             "by_status": list(by_status),
#             "overdue": overdue,
#         },
#         status=status.HTTP_200_OK,
#     )