from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('manage-users/<int:user_id>/toggle/', views.toggle_user_active, name='toggle_user_active'),
]