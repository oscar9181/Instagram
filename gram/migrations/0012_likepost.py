# Generated by Django 4.0.5 on 2022-06-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0011_alter_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
