from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from .models import Token

User = get_user_model()

class TokenBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, token=None, **kwargs):
        if token:
            try:
                token_obj = Token.objects.get(user__username=username, token=token)
            except Token.DoesNotExist:
                return None
            return token_obj.user
        return super().authenticate(request, username=username, password=password, **kwargs)