# Generated by Django 2.2.7 on 2022-06-18 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_blog_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='slug',
            new_name='blogSlug',
        ),
    ]