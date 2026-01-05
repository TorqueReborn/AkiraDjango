from django.db import models
from django.contrib.auth.models import AbstractUser

# JWT
from rest_framework_simplejwt.tokens import RefreshToken

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    token = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new and not self.token:
            refresh = RefreshToken.for_user(self)
            self.token = str(refresh)
            super().save(update_fields=['token'])

    def __str__(self):
        return self.username