from django.urls import path

from . import views


app_name = 'project'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('add/', views.add, name='add'),
    path('<uuid:pk>/', views.project, name='project'),
    path('<uuid:pk>/edit/', views.edit, name='edit'),
    path('<uuid:pk>/delete/', views.delete, name='delete'),
    path('<uuid:project_id>/files/upload/', views.upload_file, name='upload_file'),
]