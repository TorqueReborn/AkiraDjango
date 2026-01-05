# REST Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Django
from django.contrib.auth import authenticate

# Custom
from .models import Token
from .serializers import UserSerializer

class LoginView(APIView):
    def post(self, request):
        token = request.data.get('token')
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password, token=token)

        if not user:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        return Response(
            {"message": "Logged in Successfully"},
            status=status.HTTP_200_OK
        )

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        token = request.data.get('token')
        username = request.data.get('username')
        if token and username:
            try:
                token_obj = Token.objects.select_related('user').get(token=token)
                if token_obj:
                    token_obj.delete()
                    return Response({"message": "Token deleted successfully"})
            except Token.DoesNotExist:
                return Response({"message": "Unable to delete token"})
        return Response({"message": "send token and username and try again"})