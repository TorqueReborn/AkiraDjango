import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return self.username

class Token(models.Model):
    os = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    token = models.TextField(default=uuid.uuid4, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tokens')

    def __str__(self):
        return self.token