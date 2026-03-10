from django.contrib import admin

from my_app.models import Task, SubTask, Category




class SubTaskInline(admin.StackedInline):
    model = SubTask
    extra = 1



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    def short_title(self, obj):
        return (obj.title[:10] + "...") if len(obj.title) > 10 else obj.title

    short_title.short_description = "Название"

    list_display = [
        "short_title",
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

    inlines = [SubTaskInline]



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

    @admin.action(description="✅ Завершить выбранные подзадачи")
    def mark_done(self, request, queryset):
        queryset.update(status='Done')

    actions = ['mark_done']



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


