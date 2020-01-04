from django.urls import path
from .views import UserLoginAPIView, TestAPIView


urlpatterns = [
    path('login/', UserLoginAPIView.as_view()),
    path('test/', TestAPIView.as_view()),
    
]