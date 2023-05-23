from django.contrib import admin
from users.models import CustomUser
from tasks.admin import TaskAdmin


# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email', 'is_superuser', 'is_staff')
    fields = (
        'username',
        ('first_name', 'last_name'),
        'email',
        ('is_staff', 'is_superuser'),
        'image',
        ('done_tasks_count', 'die_tasks_count')
    )
    readonly_fields = ('done_tasks_count', 'die_tasks_count', 'username')
    search_fields = ('username', )
    list_filter = ('is_superuser', 'is_staff')
