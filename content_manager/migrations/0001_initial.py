# Generated by Django 3.0 on 2020-01-09 04:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('credits', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
                ('semester', models.CharField(choices=[('s1', 'Semester 1'), ('s2', 'Semester 2'), ('s3', 'Semester 3'), ('s4', 'Semester 4'), ('s5', 'Semester 5'), ('s6', 'Semester 6'), ('s7', 'Semester 7'), ('s8', 'Semester 8')], max_length=2)),
                ('department', models.CharField(choices=[('cse', 'Computer Science & Engineering'), ('ece', 'Electronics & Communication Engineering'), ('eee', 'Electrical & Electronics Engineering'), ('me', 'Mechanical Engineering'), ('ce', 'Civil Engineering')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2015)])),
                ('semester', models.CharField(choices=[('s1', 'Semester 1'), ('s2', 'Semester 2'), ('s3', 'Semester 3'), ('s4', 'Semester 4'), ('s5', 'Semester 5'), ('s6', 'Semester 6'), ('s7', 'Semester 7'), ('s8', 'Semester 8')], max_length=2)),
                ('stream', models.CharField(choices=[('regular', 'Regular'), ('supply', 'Supplymentry')], max_length=10)),
                ('link', models.CharField(max_length=500)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content_manager.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('importance', models.IntegerField()),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoLecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='VideoComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSoluntion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_link', models.CharField(blank=True, max_length=500, null=True)),
                ('QuestionPaper', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='content_manager.QuestionPaper')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('no', models.IntegerField(validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(1)])),
                ('weightage', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content_manager.Course')),
            ],
        ),
    ]