from django.shortcuts import render, HttpResponseRedirect
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from products.models import Basket
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('users:profile'))
        else:
            form = UserProfileForm(instance=request.user)

        baskets = Basket.objects.filter(user=request.user)
        total_sum = 0
        total_quantity = 0
        for basket in baskets:
            total_sum += basket.sum()
            total_quantity += basket.quantity
        context = {
            'title': 'Profile',
            'form': form,
            'baskets': baskets,
            'total_sum': total_sum,
            'total_quantity': total_quantity,
        }
        return render(request, 'users/profile.html', context)
    else:
        return HttpResponseRedirect(reverse('users:login'))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))