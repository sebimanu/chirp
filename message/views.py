# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from message.forms import RegisterForm
from message.models import Message


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = "/login"

class TimelineView(ListView):
    template_name = 'index.html'
    def get_queryset(self):
        # implement the logic
        if self.request.user.is_authenticated:
            return Message.objects.filter(user=self.request.user)
        else:
            return Message.objects.all()

class ProfileBaseView(DetailView):
    model = User
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileBaseView, self).get_context_data(**kwargs)
        context["chirps"] = Message.objects.filter(user=self.get_object())
        return context

class MyProfileView(ProfileBaseView):
    def get_object(self, queryset=None):
        return self.request.user

class ProfileView(ProfileBaseView):
    def get_slug_field(self):
        return "username"

