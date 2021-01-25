from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from app import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]