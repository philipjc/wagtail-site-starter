from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy

import sendgrid
from sendgrid.helpers.mail import *
from decouple import config


def send_enquiry(request):
    name = request.POST.get('enquiry_name', '')
    form_email = request.POST.get('enquiry_email', '')
    text = request.POST.get('enquiry_text', '')

    if form_email == '':
        raise Http404

# SendGrid API
    else:
        sg = sendgrid.SendGridAPIClient(apikey=config('SENDGRID_API_KEY'))
        from_email = Email(form_email)
        to_email = Email("filystyle@gmail.com")
        subject = "Enquiry from Drishti website"
        email_content = Content("text/plain", "Hello, " + name + " has an enquiry. \n" + text +
                                "\n My contact email is: " + str(from_email))

        new_mail = Mail(from_email, subject, to_email, email_content)
        response = sg.client.mail.send.post(request_body=new_mail.get())
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)

        return redirect(reverse_lazy('enquiry:thanks'))
