from django.contrib import admin

from .models import TaskGroup, Task

class TaskInline(admin.TabularInline):
    model = Task
    
class TaskAdminGroup(admin.ModelAdmin):
    model = TaskGroup
    inlines = [TaskInline, ] #kulang

class TaskAdmin(admin.ModelAdmin):
    model = Task
    
    search_fields = ['name', ]
    list_display = ['name', 'due_date']
    list_filter = ['due_date', 'taskgroup', ]
    
    fieldsets = [
        ('Details', {
            'fields': [
                ('name', 'due_date'), 'taskgroup'
            ]
        }
         )
    ]
    
admin.site.register(TaskGroup, TaskAdminGroup)
admin.site.register(Task, TaskAdmin)