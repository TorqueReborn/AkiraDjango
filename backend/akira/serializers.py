from .models import Favorites
from rest_framework import serializers

class FavoritesSerializer(serializers.ModelSerializer):
    animeName = serializers.CharField(source='anime.name', read_only=True)
    class Meta:
        model = Favorites
        fields = ['animeName']