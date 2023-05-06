from django.urls import path
from . import views

urlpatterns = [
    path('get-all-question-categories/', views.list_all_categories),
    path('get-all-batches-of-student/', views.list_all_batches_by_student),
    path('dashboard/', views.dashboard),
    path('question/<str:uuid>/', views.show_question_page),
    path('code-compiler/', views.compile_the_code),
    path('submit-answer/', views.submit_answer),
]