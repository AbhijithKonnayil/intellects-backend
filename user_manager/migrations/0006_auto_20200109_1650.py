# Generated by Django 3.0 on 2020-01-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0005_studentprofile_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_parent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
    ]
