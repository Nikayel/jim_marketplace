from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm
app_name = 'main_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path("signup/", views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='main_app/login.html', authentication_form=LoginForm),name='login'),
]
