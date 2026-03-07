from django.contrib import admin

from my_app.models import Task, SubTask, Category

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "status",
        "created_at",
        "deadline"
    ]

    search_fields = [
        "title",
    ]

    list_filter = [
        "created_at",
        "deadline"
    ]

    list_editable = [
        "status"
    ]

    list_per_page = 10



@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "status",
        "created_at",
        "deadline"
    ]

    search_fields = [
        "title",
    ]

    list_filter = [
        "created_at",
        "deadline"
    ]

    list_editable = [
        "status"
    ]

    list_per_page = 10



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name"
    ]

    list_display_links = [
        "id"
    ]

    search_fields = [
        "name",
    ]

    list_filter = [
        "id",
        "name"
    ]

    list_editable = [
        "name"
    ]

    list_per_page = 10


