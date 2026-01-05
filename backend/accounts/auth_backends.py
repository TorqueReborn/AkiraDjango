from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

class TokenBackend(ModelBackend):
    def authenticate(self, request, username = None, token = None, **kwargs):
        try:
            user = User.objects.get(username=username, token=token)
            return user
        except User.DoesNotExist:
            return None