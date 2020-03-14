# Generated by Django 3.0 on 2020-03-14 06:47

import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
from django.contrib.postgres.operations import HStoreExtension

class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0007_studentprofile_college'),
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='GradeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_no', models.CharField(blank=True, max_length=11, null=True)),
                ('s1', django.contrib.postgres.fields.hstore.HStoreField()),
                ('s2', django.contrib.postgres.fields.hstore.HStoreField()),
                ('s3', django.contrib.postgres.fields.hstore.HStoreField()),
                ('s4', django.contrib.postgres.fields.hstore.HStoreField()),
                ('s5', django.contrib.postgres.fields.hstore.HStoreField()),
                ('s6', django.contrib.postgres.fields.hstore.HStoreField()),
                ('s7', django.contrib.postgres.fields.hstore.HStoreField()),
                ('s8', django.contrib.postgres.fields.hstore.HStoreField()),
                ('cgpa', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='register_no',
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='grades',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_manager.GradeDetails'),
        ),
    ]