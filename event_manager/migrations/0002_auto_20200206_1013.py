# Generated by Django 3.0 on 2020-02-06 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='fees',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('workshop', 'Workshop'), ('competition', 'Competition'), ('talk', 'Talk'), ('others', 'Others')], max_length=20),
        ),
    ]
