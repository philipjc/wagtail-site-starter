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

    url(r'^(?P<pk>\d+)/profile/edit', views.UpdateProfile.as_view(), name='profile_edit'),

    url(r'^password/reset/$', auth_views.password_reset,
        {'template_name': 'password_reset.html'}, name="password_reset"),

    url(r'^password/reset/done/$', auth_views.password_reset_done,
        {'template_name': 'password_reset_done.html'}, name="password_reset_done"),

    url(r'^password/change/$', auth_views.PasswordChangeView.as_view(),
        {'template_name': 'password_change_form.html'}, name='password_change'),

    url(r'^password/change/done/$', auth_views.PasswordChangeDoneView.as_view(),
        {'template_name': 'password_change_done.html'}, name='password_change_done'),

]
