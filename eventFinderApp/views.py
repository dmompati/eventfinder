from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import UserUpdateForm, ProfileUpdateForm


class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'
    ordering = ['date_posted']

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()


class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'

class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Event
    fields = ['title', 'venue', 'location']

class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Event
    fields = ['title', 'venue', 'location']

    # def form_valid(self, form):
    #     form.instance.author = self.request.user 
    #     return super().form_valid(form)

@login_required
def account(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/my-account/')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'eventFinderApp/account.html', context)

