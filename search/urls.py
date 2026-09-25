from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidates_search, name='search.candidates_search'),
    path('send-email/', views.send_email_view, name='send_email'),
    path('filter/', views.filter_candidates, name='search.filter_candidates'),
]