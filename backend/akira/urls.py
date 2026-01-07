from django.urls import path

from .views import recent, trending, spotlight, details, watch

urlpatterns = [
    path('', recent, name='recent'),
    
    path('watch/', watch, name='watch'),
    path('details/', details, name='details'),
    path('trending/', trending, name='trending'),
    path('spotlight/', spotlight, name='spotlight'),
]