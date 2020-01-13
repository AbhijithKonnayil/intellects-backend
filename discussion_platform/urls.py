from django.urls import path, include
from .views import QuestionsListAPIView

urlpatterns = [
    path('questions/', QuestionsListAPIView.as_view(),name='question_list'),
    
]