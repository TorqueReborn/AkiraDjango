from django.urls import path

from .views import recent, trending, spotlight

urlpatterns = [
    path('', recent, name='recent'),
    
    path('trending/', trending, name='trending'),
    path('spotlight/', spotlight, name='spotlight'),
]