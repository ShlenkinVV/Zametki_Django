from django.urls import re_path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
 # Страница входа
    re_path(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'^register/$', views.register, name='register'),

]