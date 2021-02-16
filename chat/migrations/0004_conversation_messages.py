# Generated by Django 3.1.2 on 2021-02-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_conversation'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='Messages',
            field=models.ManyToManyField(related_name='texts', to='chat.Message'),
        ),
    ]