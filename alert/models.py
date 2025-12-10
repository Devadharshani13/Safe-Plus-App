from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    guardian_no = models.CharField(max_length=15)

    def __str__(self):
        return self.username