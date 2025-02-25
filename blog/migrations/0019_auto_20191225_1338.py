# Generated by Django 2.1.1 on 2019-12-25 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0018_folowers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('fromuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fromuser', to=settings.AUTH_USER_MODEL)),
                ('touser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='touser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='folowers',
            name='fromuser',
        ),
        migrations.RemoveField(
            model_name='folowers',
            name='touser',
        ),
        migrations.DeleteModel(
            name='Folowers',
        ),
    ]
