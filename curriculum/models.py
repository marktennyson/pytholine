from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.

class QuestionCategory(models.Model):
    class LANGUAGE:
        PYTHON = 0
        JAVASCRIPT = 1

    LANGUAGE_CHOICES = (
        (LANGUAGE.PYTHON, "Python"),
        (LANGUAGE.JAVASCRIPT, "Javascript")
    )
    
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    language = models.IntegerField(default=LANGUAGE.PYTHON, choices=LANGUAGE_CHOICES)
    last_modified_at = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,)

    def __str__(self):
        return f"{self.pk} - {self.name}"

class Question(models.Model):
    class LAVEL:
        EASY = 0
        MEDIUM = 1
        HARD = 2
    
    DIFFICULTY_LAVEL_CHOICES = (
        (LAVEL.EASY, "Easy"),
        (LAVEL.MEDIUM, "Medium"),
        (LAVEL.HARD, "Hard"),
    )
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(max_length=40, default=str(uuid4()))
    lavel = models.IntegerField(default=LAVEL.EASY, choices=DIFFICULTY_LAVEL_CHOICES)
    body = models.TextField(null=True, blank=True)
    category = models.ForeignKey(QuestionCategory, on_delete=models.SET_NULL, null=True, blank=True)
    marks = models.FloatField(default=1.0)
    last_modified_at = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,)

    def __str__(self):
        return f"{self.pk} - {self.name}"