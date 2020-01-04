from django.urls import path
from .views import UserLoginAPIView


urlpatterns = [
    path('login/', UserLoginAPIView.as_view()),
]