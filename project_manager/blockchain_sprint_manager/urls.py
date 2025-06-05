from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Project URLs
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/create/', views.project_create, name='project_create'),

    # Sprint URLs
    path('sprints/', views.sprint_list, name='sprint_list'),
    path('sprint/<int:pk>/', views.sprint_detail, name='sprint_detail'),
    path('sprint/create/', views.sprint_create, name='sprint_create'),
]
