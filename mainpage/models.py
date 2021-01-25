from django.db import models

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
    