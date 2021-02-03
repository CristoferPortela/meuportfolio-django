from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class AboutMe(models.Model):
    """
    About me section
    """

    ROLES_ALLOWED = (
        ('admin', 'Administrator'),
        ('empl', 'Employer')
    )

    name = models.CharField('my name', max_length=100)
    summary = models.CharField('summary', max_length=512)
    about_me = models.TextField("about me")

    role = models.CharField('role', choices=ROLES_ALLOWED, max_length=5)

    professional_xp = models.TextField('Professional experience', default="")

    welcome_title = models.CharField('title for the welcome message', max_length=155, default="")
    xp_title = models.CharField(_("title for the experiencies section"), max_length=155, default="")

    avatar = models.ImageField(
        'my pic', 
        name="avatar", 
        # width_field=150, 
        # height_field=150, 
        upload_to='uploads/%Y/%m/%d',
        null=True
    )

    def __str__(self):
        return self.name
    
class Service(models.Model):
    """
    The services we offer
    """

    title = models.CharField('service name', max_length=100)
    icon = models.CharField('icon to describe it', max_length=100)
    description = models.CharField('description', max_length=100)

    def __str__(self):
        return self.title
    

class ProjectImage(models.Model):
    """
    The url for project images
    """

    ROLES = (
        ('featured','featured',),
        ('secondary','secondary'),
    )

    title = models.CharField('the title of the image', max_length=100, default="")
    image = models.ImageField('image for the project')
    role = models.CharField('the role of the image in the page', max_length=20, choices=ROLES)

    has_call_to_action = models.BooleanField('has a call to action button?', default=False, null=True, blank=True)
    call_to_action_link = models.CharField('the call to action link', max_length=255, default="", null=True, blank=True)
    call_to_action_text = models.CharField('the call to action text', max_length=100, default="", null=True, blank=True)

    description_text = models.CharField('description of the image', max_length=255, default="", null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    """
    A category avaiable to set to the project
    """

    title = models.CharField('title of the category', max_length=50, unique=True)
    description = models.CharField('short description about the category', max_length=155)

    icon = models.CharField('an icon to represent the category', max_length=100, default="", null=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    """
    The table to represent a work or portfolio page
    """

    title = models.CharField('name of project', max_length=100)
    short_description = models.CharField('short description', max_length=155)

    full_description = models.TextField('the full description of the project', default="", null=True)

    images = models.ManyToManyField(ProjectImage)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class ProductBenefits(models.Model):
    """
    Represents a benefict of a product
    """

    title = models.CharField(max_length=75)
    description = models.CharField('the description', max_length=255)
    icon = models.CharField('define an icon', max_length=100, default="", null=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    """
    Represent the price of a kind of project, such as ecommerce, wordpress blog, etc.
    """

    title = models.CharField('the title of the project kind', max_length=100, unique=True)

    min_price = models.FloatField('the minimun price', null=True, default=0)
    avg_price = models.FloatField('an average price for the prouct', null=True, default=0)

    short_description = models.CharField('short description', max_length=100)

    benefits = models.ManyToManyField(ProductBenefits)

    def __str__(self):
        return self.title
    
class SocialMedia(models.Model):
    """
    My social medias
    """

    media = models.CharField('social media name', max_length=50)
    icon = models.CharField('the icons', max_length=100)
    link = models.CharField('the url for the social media', max_length=255)

    def __str__(self):
        return self.media    

class Contact(models.Model):
    """
    The contact model
    """

    name = models.CharField('user name', max_length=200)
    email = models.EmailField('email', max_length=254)
    subject = models.CharField('subject', max_length=255)
    message = models.TextField('message', max_length=255)

    def __str__(self):
        return self.subject

class Slider(models.Model):
    """
    A full slider
    """

    name = models.CharField('name of the slider', max_length=100)

    images = models.ManyToManyField(ProjectImage)

    def __str__(self):
        return self.name

class MainPage(models.Model):
    """
    The full model of the main page
    """

    title = models.CharField(_("Title of main page"), max_length=50)
    slider = models.ForeignKey(Slider, verbose_name=_("choose a slider"), on_delete=models.CASCADE)
    about_me = models.ForeignKey(AboutMe, verbose_name=_("choose an about me"), on_delete=models.CASCADE)
    
    services_title = models.CharField(_("servies section title"), max_length=155, default="serviços")
    services_subtitle = models.CharField(_("services section description // subtitle"), max_length=155, default="")

    services = models.ManyToManyField(Service, verbose_name=_("choose a service"))
        
    projects_title = models.CharField(_("projects section title"), max_length=155, default="Projetos")
    projects_subtitle = models.CharField(_("projects section description // subtitle"), max_length=155, default="")
    
    projects = models.ManyToManyField(Project, verbose_name=_("chosse the projects"))
    
    products_title = models.CharField(_("products section title"), max_length=155, default="Valores")
    products_subtitle = models.CharField(_("products section description // subtitle"), max_length=155, default="")
    
    products = models.ManyToManyField(Product, verbose_name=_("choose the products"))
    
    social_medias_title = models.CharField(_("social medias section title"), max_length=155, default="Redes sociais")
    social_medias_subtitle = models.CharField(_("social medias section description // subtitle"), max_length=155, default="")
    social_media_bg = models.ForeignKey(ProjectImage, on_delete=models.PROTECT, default="", blank=True, null=True)

    social_medias = models.ManyToManyField(SocialMedia, verbose_name=_("choose the social medias"))

    def __str__(self):
        return self.title

