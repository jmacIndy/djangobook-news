# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    age = models.PositiveIntegerField(default=0)
