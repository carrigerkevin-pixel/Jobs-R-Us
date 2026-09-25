from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('manage-users/<int:user_id>/toggle/', views.toggle_user_active, name='toggle_user_active'),
    path('manage-users/<int:user_id>/change-role/', views.change_user_role, name='change_user_role'),
    path('export-users/', views.export_users_csv, name='export_users_csv'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]