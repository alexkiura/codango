from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^recovery/$', views.ForgotPassword.as_view(), name='forgot_password'),
    url(r'^recovery/(?P<user_hash>([a-z0-9A-Z])+)$', views.ResetPassword.as_view(), name='reset_password'),
]