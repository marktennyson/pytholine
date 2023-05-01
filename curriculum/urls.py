from django.urls import path
from . import views

urlpatterns = [
    path('get-all-question-categories/', views.list_all_categories),
    path('get-all-batches-of-student/', views.list_all_batches_by_student),
]