# Generated by Django 4.0.5 on 2022-06-08 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0006_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gram.post'),
        ),
    ]