from django.conf.urls import url
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [

    url(r'^$', TemplateView.as_view(
        template_name='users/login_home.html'),
        name='users'),

    url(r'^login', auth_views.login, name='login'),

    url(r'^signup', views.SignUp.as_view(), name='signup'),

    # url(r'^login', views.LogIn.as_view(), name='login'),

    url(r'^(?P<pk>\d+)/profile/view', views.ViewProfile.as_view(), name='profile_view'),

    url(r'^(?P<pk>\d+)/profile/edit', views.UpdateProfile.as_view(), name='profile_edit')

]
