from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_date')
    



admin.site.register(Task, TaskAdmin)
#if you want to know which task is complited  and no complited how to do that
