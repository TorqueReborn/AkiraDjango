from django.urls import path
from .views import LogoutView, RegisterView, HomeView, login

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('home/', HomeView.as_view(), name='home'),
]