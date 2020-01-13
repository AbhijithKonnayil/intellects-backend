from rest_framework import serializers
from .models import Post, Comment, Tag


class PostSerializer(serializers.ModelSerializer):
    model = Post
    fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    model = Comment
    fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    model = Tag
    fields = '__all__'