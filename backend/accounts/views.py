# REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Django
from django.contrib.auth import authenticate

# Custom
from .models import Token
from .utils import generate_token
from .serializers import UserSerializer

@api_view(['GET'])
def home(request):
    token = request.COOKIES.get('token')
    username = request.COOKIES.get('username')
    if not username or not token:
        return Response({"message": "User not logged in"}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        token = Token.objects.get(token=token, user__username=username)
        user = token.user
        return Response({
            "First Name": user.first_name,
            "Last Name": user.last_name,
            "Username": user.username,
            "Is Active": user.is_active,
            "Date Joined": user.date_joined
        })
    except Token.DoesNotExist:
        return Response({"message": "Token invalid"}, status=status.HTTP_401_UNAUTHORIZED)

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
    response.set_cookie("username", token.user.username, samesite="None", secure=True)
    return response

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = generate_token(request, user)
        response = Response()
        response.set_cookie("token", token.token, samesite="None", secure=True)
        response.set_cookie("username", token.user.username, samesite="None", secure=True)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout(request):
    token = request.data.get('token')
    username = request.data.get('username')
    if token and username:
        try:
            token_obj = Token.objects.get(user__username=username, token=token)
            if token_obj:
                token_obj.delete()
                return Response({"message": "Token deleted successfully"})
        except Token.DoesNotExist:
            return Response({"message": "Unable to delete token"})
    return Response({"message": "send token and username and try again"})

@api_view(['GET'])
def saved_logins(request):
    print(request.COOKIES)
    return Response()