from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import HStoreField

from content_manager.choices import SEMESTER_CHOICES, DEPARTMENT_CHOICES, COLLEGE_CHOICES


class User(AbstractUser):
    def phone_validator(value):
        if len(value) != 10:
            raise ValidationError(
                ('Phone Number should have 10 digits'),)
        if not value.isdigit():
            raise ValidationError(
                ('Phone number can have only numbers'),
            )
    username = models.CharField(
        'phone', max_length=10, unique=True, validators=[phone_validator])
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        print(type(self))
        if self.is_student:
            StudentProfile.objects.create(student=self)
        if self.is_parent:
            ParentProfile.objects.create(parent=self)

    def __str__(self):
        return '{}-{}'.format(self.id, self.username)


class ParentProfile(models.Model):
    parent = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.parent.username)


class StudentProfile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    semester = semester = models.CharField(
        max_length=2, choices=SEMESTER_CHOICES, null=True, blank=True)
    department = models.CharField(
        max_length=4, choices=DEPARTMENT_CHOICES, null=True, blank=True)
    parent = models.ForeignKey(
        ParentProfile, null=True, on_delete=models.SET_NULL)
    college = models.CharField(max_length=5,choices=COLLEGE_CHOICES,default='nill')
    # grades =  models.IntegerField()

    def __str__(self):
        return '{}'.format(self.student.username)

class GradeDetails(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    register_no = models.CharField(max_length=11, null=True, blank=True)
    
