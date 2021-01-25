from datetime import datetime
from django.shortcuts import render


# Create your views here.
def home(request):
    """Renders the home page."""
    return render(
        request,
        'mainpage/index.html',
        {
            'title':'IdeiaScript',
            'year':datetime.now().year,
        }
    )
