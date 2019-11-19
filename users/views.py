from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() #saves user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been create, you are now able to login')
            return redirect ('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


