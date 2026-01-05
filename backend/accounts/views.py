# REST Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Django
from django.contrib.auth import authenticate

# Custom
from .models import Token

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