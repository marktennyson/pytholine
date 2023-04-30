from django.urls import path
from . import views

urlpatterns = [
    path('', views.editor_index_page),
    path('code-compiler/', views.compile_the_code),
]