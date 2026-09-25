from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='messaging.index'),
    path('send/', views.send_message, name='messaging.send_message'),
    path('chat/<int:id>/', views.chat, name='messaging.chat'),
    path('chat/<int:chat_id>/send/', views.send_message_in_chat, name='messaging.send_message_in_chat'),
]