from django.urls import path, include
from .views import QuestionsListAPIView, QuestionAPIView

urlpatterns = [
    path('questions/', QuestionsListAPIView.as_view(),name='question_list'),
    path('question/view/<int:id>', QuestionAPIView.as_view(),name='question_list'),

]