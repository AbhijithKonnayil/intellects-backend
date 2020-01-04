from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_406_NOT_ACCEPTABLE
)
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            user = User.objects.get(username=data.get('username'))
            serializer = UserSerializer(user)
            new_data = serializer.data
            if authenticate(request, username=data.get('username'), password=data.get('password')):
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                new_data['token'] = token.key
                return Response(new_data, status=HTTP_200_OK)
            else:
                return Response({}, status=HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({}, status=HTTP_404_NOT_FOUND)


class TestAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        print(request.user)
        return Response({"Auth ": request.user.username}, status=HTTP_200_OK)


