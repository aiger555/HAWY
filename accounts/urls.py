from django.urls import path
from .views import UserViewSet


urlpatterns = [
    path('rating/', UserViewSet, name='rating'),
]