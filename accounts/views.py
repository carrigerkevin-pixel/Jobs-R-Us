from django.shortcuts import render, get_object_or_404
from .forms import CustomUserCreationForm, ProfileEditForm
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import redirect
from .models import ApplicantProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            ApplicantProfile.objects.create(user=user)
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html',
                {'template_data': template_data})
def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            #template_data['error'] =
            #    'The username or password is incorrect.'
            return render(request, 'accounts/login.html',
                {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('accounts.profile')
@login_required
def profile(request):
    template_data = {}
    template_data['title'] = 'Profile'
    if request.user.userType == "Applicant":
        template_data['profile'] = request.user.applicantProfile
    else:
        template_data['profile'] = request.user.applicantProfile
    
    return render(request, 'accounts/profile.html',
        {'template_data': template_data})
@login_required
def editProfile(request):
    profile = get_object_or_404(ApplicantProfile, user=request.user)
    template_data = {}
    template_data['title'] = 'Edit Profile'
    if request.method == 'GET':
        template_data['form'] = ProfileEditForm(instance = profile)
        return render(request, 'accounts/editProfile.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        form = ProfileEditForm(request.POST, instance = profile)
        if form.is_valid():
            
            #applicantProfile = form.save(commit=False)
            #applicantProfile.user = request.user
            #applicantProfile.save()
            form.save()
            return redirect('accounts.profile')
        else:
            form = ProfileEditForm()
            return render(request, 'accounts/editProfile.html',
                {'template_data': template_data})
