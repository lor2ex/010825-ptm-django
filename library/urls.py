from django.contrib import admin
from django.urls import path
from rest_framework import routers

from my_app.views.categories import CategoryViewSet
from my_app.views.tasks import TaskListCreateView, TaskDetailUpdateDeleteView
from my_app.views.subtasks import SubTaskListCreateView, SubTaskDetailUpdateDeleteView

router = routers.DefaultRouter()

router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailUpdateDeleteView.as_view()),
    path('subtasks/', SubTaskListCreateView.as_view()),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view()),
]

urlpatterns += router.urls
