from accounts.models import User
from accounts.models import Token
from akira.models import Anime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def favorite(request):
    token = request.COOKIES.get('token')
    username = request.COOKIES.get('username')
    try:
        token_obj = Token.objects.get(token=token, user__username=username)
        try:
            user = User.objects.get(username=username)
            print(user)
        except User.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Token.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    return Response()