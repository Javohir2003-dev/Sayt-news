from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    STATUS = (
        ('admin', 'Admin'),
        ('reporter', 'Reporter'),
        ('writer', 'Writer'),
        )
    status = models.CharField(max_length=10, choices=STATUS, default='user')
    rasm = models.ImageField(upload_to='user/', default='user.png')
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])

    def __str__(self):
        return self.username