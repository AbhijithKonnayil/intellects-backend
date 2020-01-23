from django.shortcuts import render
from django.core.exceptions import ValidationError

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

from .serializers import PostSerializer, CommentSerializer, TagSerializer
from .models import Post, Tag, Comment


class QuestionsListAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        question_list = Post.objects.filter(post_type='q')
        serializer = PostSerializer(question_list, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class QuestionAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        question = Post.objects.get(id=kwargs['id'])
        if question.post_type != 'q':
            return Response({}, status=HTTP_404_NOT_FOUND)
        answers = question.answer_set.all()
        question_serializer = PostSerializer(question)
        answers_serializer = PostSerializer(answers, many=True)
        print("....>>",question.comment_set)
        question_comment_serializer = CommentSerializer(question.comment_set,many=True)
        answer_comment_serializer = CommentSerializer()
        return Response({"question": question_serializer.data,
                         "answers": answers_serializer.data,
                         },
                        status=HTTP_200_OK)
