# Generated by Django 5.0.6 on 2024-06-06 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='auto_id',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='auto_id',
        ),
    ]
