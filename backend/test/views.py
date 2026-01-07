from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from accounts.utils import generate_token

from accounts.models import Token

from rest_framework import status

# Django
from django.contrib.auth import authenticate

# @csrf_exempt
# @authentication_classes([])
# @permission_classes([])
@api_view(['POST'])
def test(request):
    return Response({"message": "This is test route"})

@api_view(['POST'])
def login(request):
    token = request.data.get('token')
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password, token=token)

    if not user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    token = generate_token(request, user)
    token_count = Token.objects.filter(user=user).count()

    # A user can connect only 4 devices at once
    if token_count > 4:
        Token.objects.filter(user=user).order_by('created_at').first().delete()

    response = Response()
    response.set_cookie("token", token.token, samesite="None", secure=True)
    return response