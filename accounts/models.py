from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    username = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.email = self.username
        super(CustomUser, self).save(*args, **kwargs)