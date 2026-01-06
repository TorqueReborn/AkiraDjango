from django.urls import path
from .views import test_api, cookie

urlpatterns = [
    path('', test_api),
    path('cookie/', cookie)
]