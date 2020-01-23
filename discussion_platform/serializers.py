from rest_framework import serializers
from .models import Post, Comment, Tag

from user_manager.serializers import UserLoginSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', ]


class PostSerializer(serializers.ModelSerializer):
    #question = PostSerializer()
    by = UserLoginSerializer()
    upvotes_count = serializers.SerializerMethodField()
    downvotes_count = serializers.SerializerMethodField()
    tags = TagSerializer()
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        print(" obj -- > ",CommentSerializer(obj.comment_set,many=True))
        serializer = CommentSerializer(obj.comment_set,many=True)
        return serializer.data

    def get_upvotes_count(self, obj):
        return obj.upvotes.count()

    def get_downvotes_count(self, obj):
        return obj.downvotes.count()

    class Meta:
        model = Post
        fields = ['id', 'text', 'by', 'upvotes_count',
                  'downvotes_count', 'post_type', 'tags', 'answer','comments']
        #depth = 1
