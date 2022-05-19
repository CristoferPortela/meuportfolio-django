from datetime import datetime
from django.shortcuts import render
from .models import MainPage, Project, ProjectImage, SocialMedia
# from .forms import ContactForm

# Create your views here.


def home(request):
    """
    Renders the home page
    """

    main_page = MainPage.objects.first()

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


def portfolio_item(request, id):
    project = Project.objects.get(pk=id)

    images = project.images.all() 

    social_medias = SocialMedia.objects.all()
    social_media_bg = ProjectImage.objects.last()

    return render(
        request,
        'mainpage/portfolio.html',
        {
            'project': project,
            'slider': images,
            'social_medias': social_medias,
            'social_media_bg': social_media_bg,
        }
    )
