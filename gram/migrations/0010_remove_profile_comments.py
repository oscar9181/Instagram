# Generated by Django 4.0.5 on 2022-06-08 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0009_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='comments',
        ),
    ]