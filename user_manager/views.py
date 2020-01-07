from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserLoginSerializer, UserRegisterSerializer


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            user = User.objects.get(username=data.get('username'))
            serializer = UserLoginSerializer(user)
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


class UserRegisterAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            serializer = UserRegisterSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            new_data = serializer.validated_data
            print(new_data)
            user = User.objects.create(
                username=new_data['username'],
                email=new_data['email'],
                first_name=new_data['first_name'],
                password=make_password(new_data['password'])
            )
            return Response(new_data, status=HTTP_201_CREATED)
        except :
            return Response({'msg':'Error !! User Registration Failed.'}, status=HTTP_500_INTERNAL_SERVER_ERROR)

class UserLogoutAPIView(APIView):
    authentication_classes=[TokenAuthentication,]

    def get(self,request):
        logout(request)
        return Response(status=204)

