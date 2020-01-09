from rest_framework import serializers
from .models import Course, Module, Topic, VideoLecture, VideoComment, QuestionPaper, QuestionSoluntion


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'


class VideoLectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoLecture
        fields = '__all__'


class VideoCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoComment
        fields = '__all__'


class QuestionPaperSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionPaper
        fields = '__all__'


class QuestionSolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionSoluntion
        fields = '__all__'
