# Generated by Django 2.2.7 on 2022-06-18 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_event_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-eventDate']},
        ),
    ]
