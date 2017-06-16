from django.conf.urls import url
from django.contrib.auth import views as auth_views
import views


urlpatterns = [
    url(r'register/$', views.register, name='registration'),
    url(r'login/$', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout')
]
