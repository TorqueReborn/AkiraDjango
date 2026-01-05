from django.db import models
from django.contrib.auth.models import AbstractUser

# JWT
from rest_framework_simplejwt.tokens import RefreshToken

class User(AbstractUser):

    def __str__(self):
        return self.username