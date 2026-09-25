from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Application

def is_recruiter(user):
    return user.is_authenticated and user.userType == 'Recruiter'

@login_required
@user_passes_test(is_recruiter)
def applicant_list(request):
    applications = Application.objects.select_related('applicant', 'job').all()
    return render(request, 'applications/applicant_list.html', {'applications': applications})

@login_required
@user_passes_test(is_recruiter)
def review_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    return render(request, 'applications/review_application.html', {'application': application})

@login_required
def myApplications(request):
    template_data = {}
    template_data['title'] = "My Applications"
    applications = Application.objects.filter(applicant=request.user)
    template_data['applications'] = applications
    return render(request, 'applications/myApplications.html', {'template_data':template_data})