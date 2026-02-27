from datetime import datetime

from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator



STATUS_CHOICES = [
        ('New', 'NEW STATUS'),
        ('In progress', 'IN PROGRESS STATUS'),
        ('Pending', 'PENDING STATUS'),
        ('Blocked', 'BLOCKED STATUS'),
        ('Done', 'DONE STATUS'),
    ]

class Task(models.Model):
    title: str = models.CharField(
        max_length=100,
        verbose_name="Название задачи",
        unique_for_date='created_at'
    )

    description: str = models.TextField(
        verbose_name="Описание задачи",
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(500)
        ]
    )
    categories = models.ManyToManyField(
        'Category',
        related_name='tasks',
        verbose_name="Категории задачи"
    )

    status: str = models.CharField(
        verbose_name="Статус задачи",
        max_length=20,
        choices=STATUS_CHOICES
    )
    deadline:datetime = models.DateTimeField(
        verbose_name="Дата и время дедлайн"
    )
    created_at: datetime = models.DateTimeField(
        verbose_name="Дата и время создания",
        auto_now_add=True
    )



class SubTask(models.Model):
    title: str = models.CharField(
        max_length=100,
        verbose_name="Название подзадачи"
    )

    description: str = models.TextField(
        verbose_name="Описание подзадачи",
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(500)
        ]
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.PROTECT,
        related_name='subtasks'
    )
    status: str = models.CharField(
        verbose_name="Статус задачи",
        max_length=20,
        choices=STATUS_CHOICES
    )
    deadline: datetime = models.DateTimeField(
        verbose_name="Дата и время дедлайн"
    )
    created_at: datetime = models.DateTimeField(
        verbose_name="Дата и время создания",
        auto_now_add=True
    )



class Category(models.Model):
    name: str = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название категории"
    )

