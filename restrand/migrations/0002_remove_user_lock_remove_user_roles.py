# Generated by Django 5.0 on 2025-02-21 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restrand', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='lock',
        ),
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
    ]
