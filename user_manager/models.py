from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=10, unique=True)
    USERNAME_FIELD = 'phone'
    pass


class StudentProfile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    pass


class ParentProfile(models.Model):
    parent = models.OneToOneField(User, on_delete=models.CASCADE)
    pass
