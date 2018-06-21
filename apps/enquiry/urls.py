from django.conf.urls import url
from django.views.generic import TemplateView


from .views import send_enquiry

app_name = 'enquiry'

urlpatterns = [

    url(r'^$', send_enquiry, name='send'),
    url(r'^thanks/$', TemplateView.as_view(template_name="enquiry/thankyou.html"), name='thanks'),

]
