from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import ApplicantProfile
from .forms import EmailForm
from django.core.mail import send_mail

# Create your views here.

def candidates_search(request):
    candidates = ApplicantProfile.objects.all()
    template_data = {}
    template_data['candidates'] = candidates

    return render(request, 'search/search.html', {'template_data': template_data})


def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            candidate_id = form.cleaned_data['candidate_id']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            email = form.cleaned_data['email']

            candidate = get_object_or_404(ApplicantProfile, pk=candidate_id)

            send_mail(
                subject=subject,
                message=body,
                from_email=email,
                recipient_list=[candidate.user.email],
                fail_silently=True,
            )
            return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect(request.META.get('HTTP_REFERER', '/'))


def filter_candidates(request):
    candidates = ApplicantProfile.objects.all()
    skills = request.POST.get('skills', '').strip()
    min_projects = request.POST.get('projects', '').strip()
    location = request.POST.get('location', '').strip()
    print(f"DEBUG FILTERS -> Skills: '{skills}', Location: '{location}', Projects: '{min_projects}'")   
    if skills:
        candidates = candidates.filter(skills__icontains=skills)
    if min_projects:
        candidates = candidates.filter(projects__gte=int(min_projects))
    if location:
        candidates = candidates.filter(location__icontains=location)
    
    template_data = {}
    template_data['candidates'] = candidates


    return render(request, 'search/search.html', {'template_data': template_data})