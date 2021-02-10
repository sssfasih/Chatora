# Generated by Django 3.1.2 on 2021-02-01 12:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_post_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='following',
        ),
        migrations.AddField(
            model_name='follow',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
