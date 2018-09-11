from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy

# import sendgrid
# from sendgrid.helpers.mail import *
# from decouple import config


def signup(request):
    name = request.POST.get('enquiry_name', '')
    form_email = request.POST.get('enquiry_email', '')

    if form_email == '':
        raise Http404

    else:
        return redirect(reverse_lazy('enquiry:thanks'))

