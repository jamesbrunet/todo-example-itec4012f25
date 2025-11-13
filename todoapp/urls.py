from django.urls import path
from . import views

urlpatterns = [
    path('api/task_list', views.task_list, name='task_list'),
    path('api/tasks/<int:pk>/', views.task_delete, name='task_delete'),
    path('api/tasks/<int:pk>/toggle/', views.task_toggle, name='task_toggle'),
]