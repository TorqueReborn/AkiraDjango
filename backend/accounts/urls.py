from django.urls import path
from .views import logout, register, home, login

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
]