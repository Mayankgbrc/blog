# Generated by Django 2.1.1 on 2020-05-22 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0043_auto_20200516_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover_image_src',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
