# Generated by Django 3.0 on 2020-01-09 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0004_auto_20200109_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_manager.ParentProfile'),
        ),
    ]
