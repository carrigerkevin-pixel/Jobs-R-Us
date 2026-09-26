from django.db import models
from accounts.models import User

class Job(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posted_jobs")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    onSite = models.BooleanField()
    #salaryRange = models.CharField(max_length=200, blank=True)
    minSalary = models.PositiveIntegerField(blank=True)
    maxSalary = models.PositiveIntegerField(blank=True)
    visaSponsorship = models.BooleanField()
    skills = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
