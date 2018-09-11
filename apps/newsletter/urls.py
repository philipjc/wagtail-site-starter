from django.conf.urls import url
from django.views.generic import TemplateView


from .views import signup

app_name = 'newsletter'

urlpatterns = [

    url(r'^$', signup, name='signup'),
    url(r'^thanks/$', TemplateView.as_view(template_name="newsletter/thankyou.html"), name='thanks'),

]
