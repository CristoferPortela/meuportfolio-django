from datetime import datetime
from django.shortcuts import render
from .models import AboutMe

# Create your views here.
def home(request):
    """Renders the home page."""

    me = AboutMe.objects.filter(role='admin').first()

    print(me)

    return render(
        request,
        'mainpage/index.html',
        {
            'title':'IdeiaScript',
            'year':datetime.now().year,
            'about_me':me,
        }
    )
