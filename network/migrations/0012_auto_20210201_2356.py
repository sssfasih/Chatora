# Generated by Django 3.1.2 on 2021-02-01 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_auto_20210201_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='following',
        ),
        migrations.AddField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='following', to='network.user'),
            preserve_default=False,
        ),
    ]
