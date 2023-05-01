from django.urls import path
from . import views

urlpatterns = [
    path('question-listing/', views.question_listing),
    path('dashboard/', views.dashboard),
]