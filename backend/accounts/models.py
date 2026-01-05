from django.db import models
from django.contrib.auth.models import AbstractUser

# JWT
from rest_framework_simplejwt.tokens import RefreshToken

class User(AbstractUser):
    def __str__(self):
        return self.username

class Token(models.Model):
    token = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tokens')

    def __str__(self):
        return self.token