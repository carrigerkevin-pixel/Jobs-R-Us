from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Application

def is_recruiter(user):
    return user.is_authenticated and user.userType == 'Recruiter'

@login_required
@user_passes_test(is_recruiter)
def applicant_list(request):
    applications = Application.objects.select_related('applicant', 'job').all()
    template_data = {'title': 'Applicants'}
    return render(request, 'applications/applicant_list.html', {'applications': applications, 'template_data': template_data,})

@login_required
@user_passes_test(is_recruiter)
def review_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    template_data = {'title': f'{application.applicant.fullName} - Review'}
    return render(request, 'applications/review_application.html', {'application': application, 'template_data': template_data})

@login_required
@user_passes_test(is_recruiter)
def change_application_status(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        valid_statuses = [choice[0] for choice in Application.Status.choices]
        if new_status in valid_statuses:
            application.status = new_status
            application.save()
    return redirect('review_application', application_id=application.id)