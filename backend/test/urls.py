from django.urls import path
from .views import test_api, set_cookie, create_session

urlpatterns = [
    path('', test_api),
    path('set_cookie/', set_cookie),
    path('create_session/', create_session)
]