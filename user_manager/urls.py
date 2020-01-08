from django.urls import path, include
from rest_auth.views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView
)
from .views import UserLoginAPIView, UserRegisterAPIView, UserLogoutAPIView

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(),name='user_login'),
    path('register/', UserRegisterAPIView.as_view(),name='user_register'),
    path('logout/', UserLogoutAPIView.as_view(),name='user_logout'),

    path('password/change/', PasswordChangeView.as_view(),name='password_change'),
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]
