from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_500_INTERNAL_SERVER_ERROR
)

from .serializers import PostSerializer
from .models import Post, Tag, Comment

class QuestionsListAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        question_list = Post.objects.filter(post_type='q')
        serializer = PostSerializer(question_list,many=True)
        return Response(serializer.data,status=HTTP_200_OK)

