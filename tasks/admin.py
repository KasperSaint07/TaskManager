from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status', 'deadline', 'created_at')
    list_filter = ('status', 'deadline', 'owner')
    search_fields = ('title', 'description', 'owner__username')

admin.site.register(Task, TaskAdmin)
