from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

# Create your views here.
def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        group = request.POST.get('group') # student
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, 'Invalid credentials')
                redirect('slogin')
            else:
                # if user is a student
                if user.groups.filter(name=group).exists():
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'You are not a student')
                    return redirect('slogin')
        else:
            messages.error(request, 'Please fill all fields')
    return render(request, 'accounts/student/login.html')

def student_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        group = request.POST['group']
        if pwd1 == pwd2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=pwd1)
                user.save()
                group = Group.objects.get(name=group)
                user.groups.add(group)
                messages.success(request, 'Account successfully created')
                return redirect('slogin')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'accounts/student/register.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
       profile = Profile.objects.filter(user=request.user).first()
       if profile:
            form = ProfileForm(instance=profile)
       else:
           form = ProfileForm()
    return render(request, 'accounts/create_profile.html', {'form': form})
