# Generated by Django 3.0 on 2020-03-14 12:08

import django.contrib.postgres.fields.hstore
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0010_auto_20200314_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradedetails',
            name='cgpa',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='gradedetails',
            name='s1',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gradedetails',
            name='s2',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gradedetails',
            name='s3',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gradedetails',
            name='s4',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gradedetails',
            name='s5',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gradedetails',
            name='s6',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gradedetails',
            name='s7',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gradedetails',
            name='s8',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True),
        ),
    ]
