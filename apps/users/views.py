from django.urls import reverse_lazy
from django.views import generic
from django import template


from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class LogIn(generic.CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'login.html'
