from django.urls import path
from . import views

urlpatterns = [
   path('jobsList/', views.jobsList, name='jobs.jobsList'),
   #path('jobsResults/' views.jobsResults, name='jobs.jobsResults')
]