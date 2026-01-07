from django.urls import path

from .views import recent, trending, spotlight, details

urlpatterns = [
    path('', recent, name='recent'),
    
    path('details/', details, name='details'),
    path('trending/', trending, name='trending'),
    path('spotlight/', spotlight, name='spotlight'),
]