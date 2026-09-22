from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import ApplicantProfile
#fix since more than one profile type
def home(request):
    return render(request, 'core/home.html')

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def manage_users(request):
    users = User.objects.all()
    for user in users:
        ApplicantProfile.objects.get_or_create(user=user)
    return render(request, 'core/manage_users.html', {'users': users})

@login_required
@user_passes_test(is_admin)
def toggle_user_active(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = not user.is_active
    user.save()
    return redirect('manage_users')

@login_required
@user_passes_test(is_admin)
def change_user_role(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile, created = ApplicantProfile.objects.get_or_create(user=user)
    if request.method == 'POST':
        new_role = request.POST.get('role')
        if new_role in ['seeker', 'recruiter']:
            profile.role = new_role
            profile.save()
    return redirect('manage_users')
