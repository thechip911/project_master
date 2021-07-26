from django.contrib import admin

# Register your models here.
from projects.models import Project, Task, TimeSheet


@admin.register(Project)
class Projects(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_by', 'created']

    fields = ['name', 'team', 'is_archived']

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ['id', 'name', 'total_task_time', 'created_by', 'created', 'task_status', 'task_priority']

    list_editable = ['task_status', 'task_priority']

    fields = ['name', 'project', 'due_date', 'task_status', 'task_priority', 'assigned_to']

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()


@admin.register(TimeSheet)
class TimeEntry(admin.ModelAdmin):
    list_display = ['id', 'sys_id', 'task', 'start_time', 'end_time', 'duration', 'created_by', 'created']

    fields = ['task', 'start_time', 'end_time']

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()
