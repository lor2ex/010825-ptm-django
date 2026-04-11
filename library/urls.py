from django.contrib import admin
from django.urls import path

from my_app.views.tasks import TaskListCreateView, TaskDetailUpdateDeleteView
from my_app.views.subtasks import SubTaskListCreateView, SubTaskDetailUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailUpdateDeleteView.as_view()),
    path('subtasks/', SubTaskListCreateView.as_view()),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view()),
]

