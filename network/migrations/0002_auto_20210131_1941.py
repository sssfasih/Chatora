# Generated by Django 3.1.2 on 2021-01-31 14:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('likes', models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
