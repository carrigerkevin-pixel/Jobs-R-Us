from django.contrib import admin
from .models import ApplicantProfile, User

admin.site.register(User)
admin.site.register(ApplicantProfile)