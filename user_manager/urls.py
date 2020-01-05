from django.urls import path
from .views import UserLoginAPIView, UserRegisterAPIView, UserLogoutAPIView


urlpatterns = [
    path('login/', UserLoginAPIView.as_view()),
    path('register/', UserRegisterAPIView.as_view()),
    path('logout/', UserLogoutAPIView.as_view()),
    
]