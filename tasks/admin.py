from django.contrib import admin
from tasks.models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_done', 'is_die')
    fields = (
        'title',
        'description',
        'user',
        ('created_at', 'deadline'),
        ('is_done', 'is_die'),
    )
    readonly_fields = ('title', 'description', 'user', 'created_at', 'deadline', 'is_done', 'is_die')
    search_fields = ('user', )
    list_filter = ('is_done', 'is_die')
