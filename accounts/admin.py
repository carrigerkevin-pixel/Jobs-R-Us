from django.contrib import admin
from .models import ApplicantProfile, RecruiterProfile, User

admin.site.register(User)
admin.site.register(ApplicantProfile)
admin.site.register(RecruiterProfile)