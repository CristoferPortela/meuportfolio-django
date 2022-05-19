# Generated by Django 4.0.4 on 2022-05-11 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='my name')),
                ('summary', models.CharField(max_length=512, verbose_name='summary')),
                ('about_me', models.TextField(verbose_name='about me')),
                ('role', models.CharField(choices=[('admin', 'Administrator'), ('empl', 'Employer')], max_length=5, verbose_name='role')),
                ('professional_xp', models.TextField(default='', verbose_name='Professional experience')),
                ('welcome_title', models.CharField(default='', max_length=155, verbose_name='title for the welcome message')),
                ('xp_title', models.CharField(default='', max_length=155, verbose_name='title for the experiencies section')),
                ('avatar', models.ImageField(null=True, upload_to='uploads/%Y/%m/%d', verbose_name='my pic')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='title of the category')),
                ('description', models.CharField(max_length=155, verbose_name='short description about the category')),
                ('icon', models.CharField(default='', max_length=100, null=True, verbose_name='an icon to represent the category')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='user name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('subject', models.CharField(max_length=255, verbose_name='subject')),
                ('message', models.TextField(max_length=255, verbose_name='message')),
            ],
        ),
        migrations.CreateModel(
            name='ProductBenefits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=255, verbose_name='the description')),
                ('icon', models.CharField(default='', max_length=100, null=True, verbose_name='define an icon')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='the title of the image')),
                ('image', models.ImageField(upload_to='', verbose_name='image for the project')),
                ('role', models.CharField(choices=[('featured', 'featured'), ('secondary', 'secondary')], max_length=20, verbose_name='the role of the image in the page')),
                ('has_call_to_action', models.BooleanField(blank=True, default=False, null=True, verbose_name='has a call to action button?')),
                ('call_to_action_link', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='the call to action link')),
                ('call_to_action_text', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='the call to action text')),
                ('description_text', models.CharField(default='', max_length=255, null=True, verbose_name='description of the image')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='service name')),
                ('icon', models.CharField(max_length=100, verbose_name='icon to describe it')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.CharField(max_length=50, verbose_name='social media name')),
                ('icon', models.CharField(max_length=100, verbose_name='the icons')),
                ('link', models.CharField(max_length=255, verbose_name='the url for the social media')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name of the slider')),
                ('images', models.ManyToManyField(to='mainpage.projectimage')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='name of project')),
                ('short_description', models.CharField(max_length=155, verbose_name='short description')),
                ('full_description', models.TextField(default='', null=True, verbose_name='the full description of the project')),
                ('category', models.ManyToManyField(to='mainpage.category')),
                ('images', models.ManyToManyField(to='mainpage.projectimage')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='the title of the project kind')),
                ('min_price', models.FloatField(default=0, null=True, verbose_name='the minimun price')),
                ('avg_price', models.FloatField(default=0, null=True, verbose_name='an average price for the prouct')),
                ('short_description', models.CharField(max_length=100, verbose_name='short description')),
                ('benefits', models.ManyToManyField(to='mainpage.productbenefits')),
            ],
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title of main page')),
                ('services_title', models.CharField(default='serviços', max_length=155, verbose_name='servies section title')),
                ('services_subtitle', models.CharField(default='', max_length=155, verbose_name='services section description // subtitle')),
                ('projects_title', models.CharField(default='Projetos', max_length=155, verbose_name='projects section title')),
                ('projects_subtitle', models.CharField(default='', max_length=155, verbose_name='projects section description // subtitle')),
                ('products_title', models.CharField(default='Valores', max_length=155, verbose_name='products section title')),
                ('products_subtitle', models.CharField(default='', max_length=155, verbose_name='products section description // subtitle')),
                ('social_medias_title', models.CharField(default='Redes sociais', max_length=155, verbose_name='social medias section title')),
                ('social_medias_subtitle', models.CharField(default='', max_length=155, verbose_name='social medias section description // subtitle')),
                ('about_me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.aboutme', verbose_name='choose an about me')),
                ('products', models.ManyToManyField(to='mainpage.product', verbose_name='choose the products')),
                ('projects', models.ManyToManyField(to='mainpage.project', verbose_name='chosse the projects')),
                ('services', models.ManyToManyField(to='mainpage.service', verbose_name='choose a service')),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.slider', verbose_name='choose a slider')),
                ('social_media_bg', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='mainpage.projectimage')),
                ('social_medias', models.ManyToManyField(to='mainpage.socialmedia', verbose_name='choose the social medias')),
            ],
        ),
    ]