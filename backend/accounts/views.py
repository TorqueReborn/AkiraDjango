# REST Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Django
from django.contrib.auth import authenticate

# JWT
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        token = RefreshToken.for_user(user)
        access_token = str(token.access_token)

        response = Response(
            {"access_token": access_token},
            status=status.HTTP_200_OK
        )

        response.set_cookie(
            key='refresh_token',
            value=str(token),
            httponly=True,
            secure=True,
            samesite="Strict",
            path="/api/refresh/"
        )
        
        return response

class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')

        if not refresh_token:
            return Response(
                {'error': 'No refresh token'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            return Response({"access_token": access_token})
        except Exception:
            return Response(
                {'error': 'Invalid refresh token'},
                status=status.HTTP_401_UNAUTHORIZED
            )