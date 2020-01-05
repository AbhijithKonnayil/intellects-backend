from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import HStoreField


class User(AbstractUser):
    def phone_validator(value):
        if len(value) != 10:
            raise ValidationError(
                ('Phone Number should have 10 digits'),)
        if not value.isdigit():
            raise ValidationError(
                ('Phone number can have only numbers'),
                )
    username = models.CharField('phone', max_length=10, unique=True,validators=[phone_validator])

class StudentProfile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    # grades =  models.IntegerField()

    def __str__(self):
        return '{}'.format(self.student.username)


class ParentProfile(models.Model):
    parent = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.parent.username)
