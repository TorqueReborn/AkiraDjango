from django.urls import path

from .views import recent, trending

urlpatterns = [
    path('', recent, name='recent'),
    path('trending/', trending, name='trending'),
]