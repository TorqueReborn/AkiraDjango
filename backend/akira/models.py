from django.db import models
from accounts.models import User

class Anime(models.Model):
    animeId = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return self.anime.name