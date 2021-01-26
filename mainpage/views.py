from datetime import datetime
from django.shortcuts import render
from .models import AboutMe, Service

# Create your views here.
def home(request):
    """Renders the home page."""

    me = AboutMe.objects.filter(role='admin').first()
    services = Service.objects.all()

    return render(
        request,
        'mainpage/index.html',
        {
            'title':'IdeiaScript',
            'year':datetime.now().year,
            'about_me':me,
            'services': services
        }
    )
