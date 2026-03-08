import os
from datetime import timedelta, datetime
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()

from my_app.models import Task, SubTask


new_task = Task.objects.create(
    title="Prepare presentation",
    description="Prepare materials and slides for the presentation",
    status="New",
    deadline=datetime.now() + timedelta(days=3)
)
new_subtasks = [
    SubTask(
        title="Gather information",
        description="Find necessary information for the presentation",
        status="New",
        deadline=datetime.now() + timedelta(days=2),
        task=new_task
    ),
    SubTask(
        title="Create slides",
        description="Create presentation slides",
        status="New",
        deadline=datetime.now() + timedelta(days=1),
        task=new_task
    ),
]
SubTask.objects.bulk_create(new_subtasks)
print("create done")

tasks_new = Task.objects.filter(status="New")
subtasks_overdue_done = SubTask.objects.filter(
    status="Done",
    deadline__lt=datetime.now().date()
)
print("read done")

Task.objects.filter(title="Prepare presentation").update(status="In progress")
SubTask.objects.filter(title="Gather information").update(deadline=datetime.now() + timedelta(days=-2))
SubTask.objects.filter(title="Create slides").update(description="Create and format presentation slides")
print("update done")

SubTask.objects.filter(task__title="Prepare presentation").delete()
Task.objects.filter(title="Prepare presentation").delete()
print("delete done")




