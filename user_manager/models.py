from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import HStoreField


class User(AbstractUser):
    username = models.CharField('phone', max_length=10, unique=True)
    pass


class StudentProfile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    #grades =  models.IntegerField()

    def __str__(self):
        return '{}'.format(self.student.username)

class ParentProfile(models.Model):
    parent = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.student.username)
