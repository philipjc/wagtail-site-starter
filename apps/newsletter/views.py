from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

from .models import NewsLetterSubscriber


def news_signup(request):

    validator = EmailValidator()
    form_email = request.POST.get('newsletter_email', '')

    try:
        validator(form_email)
        valid_email = True

    except ValidationError:
        valid_email = False

    if not valid_email:
        print("invalid email")
        raise Http404

    else:

        try:
            subscriber = NewsLetterSubscriber(email=form_email)
            subscriber.save()

            return redirect(reverse_lazy('newsletter:thanks'))

        except Exception as error:
            print("Failed to save new subscriber", error)
            raise Http404
