from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    display_name = models.CharField(max_length=20, blank=True, null=True)

    REQUIRED_FIELDS = ['display_name']

    def __str__(self):
        return self.username