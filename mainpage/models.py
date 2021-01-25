from django.db import models

# Create your models here.

class AboutMe(models.Model):
    """
    About me section
    """

    name = models.CharField('my_name', max_length=100)
    summary = models.CharField('summary', max_length=255)
    about_me = models.TextField("about_me")

    pic = models.ImageField('my_pic', width_field=150, height_field=150)

    def __str__(self):
        return self.name
    