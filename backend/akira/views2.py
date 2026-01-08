from accounts.models import User
from accounts.models import Token

from akira.models import Anime
from akira.models import Favorites
from .serializers import FavoritesSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def favorite(request):
    token = request.COOKIES.get('token')
    username = request.COOKIES.get('username')

    animeId = request.data.get('animeId')
    animeName = request.data.get('name')
    try:
        Token.objects.get(token=token, user__username=username)
        try:
            user = User.objects.get(username=username)
            anime = Anime.objects.get_or_create(animeId=animeId, name=animeName)
            Favorites.objects.get_or_create(user=user, anime=anime[0])
        except User.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Token.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    return Response()

@api_view(['GET'])
def favorites(request):
    token = request.COOKIES.get('token')
    username = request.COOKIES.get('username')

    try:
        Token.objects.get(token=token, user__username=username)
        try:
            user = User.objects.get(username=username)
            favorites = Favorites.objects.filter(user=user)
            serializer = FavoritesSerializer(favorites, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Token.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
