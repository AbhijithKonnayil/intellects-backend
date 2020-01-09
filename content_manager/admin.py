from django.contrib import admin
from .models import Course, Module, Topic, VideoLecture, VideoComment, QuestionPaper, QuestionSoluntion

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Topic)
admin.site.register(VideoLecture)
admin.site.register(VideoComment)
admin.site.register(QuestionPaper)
admin.site.register(QuestionSoluntion)