from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import forms, views

urlpatterns = [
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.AuthForm,
             extra_context={'title': 'Entrar na minha conta'}
         ),
        name='login'
    ),
    path('register', views.register, name="register"
    ),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]