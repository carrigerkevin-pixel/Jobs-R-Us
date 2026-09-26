from django.urls import path
from . import views

urlpatterns = [
   path('', views.applicant_list, name='applicant_list'),
   path('<int:application_id>/', views.review_application, name='review_application'),
   path('<int:application_id>/status/', views.change_application_status, name='change_application_status'),
]