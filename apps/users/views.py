from django.urls import reverse_lazy
from django.views import generic
from django import template
from django.shortcuts import redirect, render
from django.http import request

from .forms import CustomUserCreationForm, UpdateProfileForm
from .models import CustomUser, Profile


class SignUp(generic.CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class LogIn(generic.CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'login.html'


class ViewProfile(generic.TemplateView):

    model = Profile
    template_name = 'profile.html'


class UpdateProfile(generic.FormView):

    model = Profile
    form_class = UpdateProfileForm
    success_url = reverse_lazy('profile_view')
    template_name = 'profile_edit.html'

    def post(self, request, pk):

        try:
            profile = Profile.objects.get(user=request.user)
            # if it's a OneToOne field, you can do:
            # profile = request.user.myprofile

            f = UpdateProfileForm(request.POST, instance=profile)
            if f.is_valid():
                f.save()
                return redirect('profile_view', pk=request.user.id)

        except Profile.DoesNotExist:
            profile = None
            # other code that handles missing profile

        print(profile)

        return render(request, self.template_name)

