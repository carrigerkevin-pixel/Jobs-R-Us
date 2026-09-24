from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='messaging.index'),
    path('send/', views.send_message, name='messaging.send_message'),
]