from django.urls import path
from . import views

urlpatterns = [
    path('', views.editor_index_page),
    path('compile-the-code/', views.compile_the_code),
]