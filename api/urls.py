from django.urls import path
from .views import HouseAPIView

urlpatterns = [
    path('houses/', HouseAPIView.as_view(), name='house-list'),
]