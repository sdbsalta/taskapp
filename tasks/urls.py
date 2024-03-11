# tasks/urls.py
from django.urls import path
from .views import task_list, task_detail, TaskListView, TaskDetailView

urlpatterns = [
    path('list', TaskListView.as_view(), name='list'),
    path('<int:pk>/detail', TaskDetailView.as_view(), name='task-detail'),
]

app_name = 'tasks'