from django.db import models
from accounts.models import ApplicantProfile
from jobs.models import Job

class Application(models.Model):
    class Status(models.TextChoices):
        APPLIED = "Applied"
        REVIEW = "Review"
        INTERVIEW = "Interview"
        OFFER = "Offer"
        CLOSED = "Closed"
    
    applicant = models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE, related_name="applications")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    note = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.APPLIED)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.fullName} -> {self.job.title}"
