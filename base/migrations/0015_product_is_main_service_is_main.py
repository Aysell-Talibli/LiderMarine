# Generated by Django 4.2.3 on 2023-07-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_about_text_az_about_text_en_about_text_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Ana sehifede gorunsun?'),
        ),
        migrations.AddField(
            model_name='service',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Ana sehifede gorunsun?'),
        ),
    ]
