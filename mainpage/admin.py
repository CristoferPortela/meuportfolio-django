from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.AboutMe)
admin.site.register(models.Service)
admin.site.register(models.Category)
admin.site.register(models.Project)
admin.site.register(models.ProductBenefits)
admin.site.register(models.Product)
admin.site.register(models.SocialMedia)
admin.site.register(models.MainPage)

