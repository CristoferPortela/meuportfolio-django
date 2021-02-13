from django.db import models

# Create your models here.

class ImageMedia(models.Model):
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

class Slider(models.Model):
    """
    A full slider
    """

    name = models.CharField('name of the slider', max_length=100)

    images = models.ManyToManyField(ImageMedia)

    def __str__(self):
        return self.name
