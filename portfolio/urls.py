"""
Definition of urls for portfolio.
"""

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('app.urls')),
    path('', include('mainpage.urls')),
    path('admin/', admin.site.urls),
]
