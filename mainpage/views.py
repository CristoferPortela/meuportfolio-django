from datetime import datetime
from django.shortcuts import render
from .models import AboutMe, Service, Project, Product, SocialMedia, Slider, MainPage
from .forms import ContactForm

# Create your views here.
def home(request):
    """
    Renders the home page
    """
    
    try: 

        main_page = MainPage.objects.first()

        contact_form = ContactForm

        return render(
            request,
            'mainpage/index.html',
            {
                'title': main_page.title,
                'about_me': main_page.about_me,
                'services': main_page.services.all(),
                'projects': main_page.projects.all(),
                'products': main_page.products.all()[:3],
                'social_medias': main_page.social_medias.all()[:6],
                'social_media_bg': main_page.social_media_bg,
                'contact_form': contact_form,
                'slider': main_page.slider.images.all(),
                'texts': {
                    'services_title': main_page.services_title,
                    'services_subtitle': main_page.services_subtitle,
                    'projects_title': main_page.projects_title,
                    'projects_subtitle': main_page.projects_subtitle,
                    'products_title': main_page.products_title,
                    'products_subtitle': main_page.products_subtitle,
                    'social_medias_title': main_page.social_medias_title,
                    'social_medias_subtitle': main_page.social_medias_subtitle,
                }
            }
        )
    except:
        return render(request, 'mainpage/index.html')

def portfolio_item(request, id):
    return render(
        request,
        'mainpage/portfolio.html',
        {'id': id}
    )

def portfolio(request, id):
    return render(
        request,
        'mainpage/portfolio.html',
        {'id': id}
    )