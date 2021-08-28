from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm, CreateProfile
from .models import Profile


def register(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'user/user_register.html', context)


def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                print(username, password)
                login(request, user)
                return redirect('home')
    context = {'form': form}
    return render(request, 'user/user_login.html', context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def get_profile(request, user_id):
    try:
        profile = Profile.objects.get(user_id=request.user.id)
    except Profile.DoesNotExist:
        return redirect('home')
    return render(request, 'user/user_profile.html', {'profile': profile})


@login_required
def update_profile(request, user_id):
    try:
        profile = Profile.objects.get(user_id=request.user.id)
    except Profile.DoesNotExist:
        return redirect('home')
    form = CreateProfile(instance=profile)
    if request.method == 'POST':
        form = CreateProfile(request.POST, instance=profile)
        print(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile = form.save(commit=False)
            if request.FILES.get('image', None) is not None:
                profile.image = request.FILES['image']
            profile.save()
            return redirect('profile', user_id)
    return render(request, 'user/user_profile_update.html', {'profile': form})
