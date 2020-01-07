from django.urls import path, include
from rest_auth.views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView
)
from .views import UserLoginAPIView, UserRegisterAPIView, UserLogoutAPIView



# urlpatterns = [
#     url(r'^password/change/$', PasswordChangeView.as_view(),
#         name='rest_password_change'),
# ]

urlpatterns = [
    path('login/', UserLoginAPIView.as_view()),
    path('register/', UserRegisterAPIView.as_view()),
    path('logout/', UserLogoutAPIView.as_view()),

    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/<uidb64>-<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]
