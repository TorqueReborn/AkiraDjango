from django.urls import path

from .views import recent

urlpatterns = [
    path('', recent, name='recent'),
]