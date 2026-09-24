import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test

User = get_user_model()
def home(request):
    return render(request, 'core/home.html')

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def manage_users(request):
    users = User.objects.all()
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
    if request.method == 'POST':
        new_role = request.POST.get('role')
        if new_role in [User.UserType.APPLICANT, User.UserType.RECRUITER]:
            user.userType = new_role
            user.save()
    return redirect('manage_users')

@login_required
@user_passes_test(is_admin)
def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="jobsrus_users.csv"'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Email', 'Role', 'Active', 'Date Joined'])
    for user in User.objects.all():
        writer.writerow([user.username, user.email, user.userType, user.is_active, user.date_joined,])
    return response
