# django import
from django.urls import path

# app label
from projects.views import ProjectCreateView, ProjectDashBoard, ProjectDeleteView, ProjectUpdateView, TaskCreateView, \
    TaskDashBoard, \
    TaskDeleteView, TaskUpdateView, TimeSheetCreateView, \
    TimeSheetDashBoard, TimeSheetUpdateView

# local view import

app_name = 'projects'

urlpatterns = [
    path('project_create/', ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project_dashboard/', ProjectDashBoard.as_view(), name='project_dashboard'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('task_create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task_dashboard/', TaskDashBoard.as_view(), name='task_dashboard'),
    path('time_sheet_create/', TimeSheetCreateView.as_view(), name='time_sheet_create'),
    path('time_sheet/<int:pk>/update/', TimeSheetUpdateView.as_view(), name='time_sheet_update'),
    path('time_sheet_dashboard/', TimeSheetDashBoard.as_view(), name='time_sheet_dashboard'),
]
