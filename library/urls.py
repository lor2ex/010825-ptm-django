from django.contrib import admin
from django.urls import path

from my_app.views.tasks import get_all_tasks, get_task_by_id, create_new_task, get_tasks_statistic
from my_app.views.subtasks import SubTaskListCreateView, SubTaskDetailUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', get_all_tasks),
    path('tasks/<int:pk>', get_task_by_id),
    path('tasks/create/', create_new_task),
    path('tasks/statistic/', get_tasks_statistic),
    path('subtasks/', SubTaskListCreateView.as_view()),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view()),
]
