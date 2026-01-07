from django.urls import path
from .views import login, test

urlpatterns = [
    path('login/', login, name='login'),
    path('test/', test, name='test'),
]