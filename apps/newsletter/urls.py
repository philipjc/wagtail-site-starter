from django.conf.urls import url
from django.views.generic import TemplateView


from .views import news_signup

app_name = 'newsletter'

urlpatterns = [

    url(r'^$', news_signup, name='signup'),
    url(r'^thanks/$', TemplateView.as_view(template_name="newsletter/thankyou.html"), name='thanks'),

]
