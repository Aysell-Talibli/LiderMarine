# Generated by Django 4.2.3 on 2023-07-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_homeimage_main_slider_socialmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='footer_logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='main',
            name='header_logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
