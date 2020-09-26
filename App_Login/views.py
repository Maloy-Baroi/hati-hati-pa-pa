from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import SignUpForm, UserProfileChangeForm, ProfilePicForm
from App_Blog.models import Blog
from App_Login.models import UserProfile


# Create your views here.
def signup(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    diction = {'form': form, 'registered': registered}
    return render(request, "App_Login/signup.html", context=diction)


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user=user)
                return HttpResponseRedirect(reverse('App_Blog:home'))

    return render(request, 'App_Login/login.html', context={'form': form})


@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))


@login_required
def profile(request):
    blog = Blog.objects.all()
    return render(request, "App_Login/profile.html", context={'blog': blog})


@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChangeForm(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChangeForm(instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, "App_Login/change_profile.html", context={'form': form})


@login_required(login_url='App_Login:login')
def pass_change(request):
    chng = False
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            chng = True

    return render(request, "App_Login/pass_change.html", context={'form': form, 'change': chng})


@login_required(login_url='App_Login:login')
def add_profile_picture(request):
    form = ProfilePicForm()
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES)
        print(request.user)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, "App_Login/add_profile_picture.html", context={'form': form})


@login_required
def change_pro_pic(request):
    form = ProfilePicForm(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, "App_Login/add_profile_picture.html", context={'form': form})

