from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from .models import Token

User = get_user_model()

class TokenBackend(ModelBackend):
    def authenticate(self, request, username = None, password=None, token = None, **kwargs):
        if token:
            try:
                token_obj = Token.objects.select_related('user').get(token=token)
            except Token.DoesNotExist:
                return None
            
            user = token_obj.user

            if username and user.username != username:
                return None
            
            return user
        
        return super().authenticate(request, username=username, password=password, **kwargs)