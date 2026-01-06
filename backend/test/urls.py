from django.urls import path
from .views import test_api, set_cookie

urlpatterns = [
    path('', test_api),
    path('set_cookie/', set_cookie)
]