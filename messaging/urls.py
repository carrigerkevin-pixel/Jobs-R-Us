from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='messaging.index'),
<<<<<<< HEAD
    path('send/', views.send_message, name='messaging.send_message'),
=======
>>>>>>> d607ca8bc7f5468fbbfa8dbbf9099af92dc6c52c
]