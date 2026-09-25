from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class UserType(models.TextChoices):
        APPLICANT = "Applicant"
        RECRUITER = "Recruiter"

    userType = models.CharField(
        max_length=20,
        choices=UserType.choices
    )

class ApplicantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="applicantProfile")
    fullName= models.CharField(max_length=200, default="Full Name")
    headline = models.CharField(max_length=200, blank=True)
    skills = models.CharField(max_length=300, blank=True)
    education = models.TextField(blank=True)
    work_experience = models.TextField(blank=True)
    links = models.URLField(blank=True)
    is_profile_private = models.BooleanField(default=False)
    location = models.CharField(max_length=200, blank=False)
    projects = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.fullName} "

class RecruiterProfile(models.Model):
    recruiter = models.OneToOneField(User, on_delete=models.CASCADE, related_name="recruiterProfile")