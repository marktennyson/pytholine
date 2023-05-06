from django.db import models
from uuid import uuid4
from datetime import datetime
from django.contrib.auth.models import User
from typing import Optional

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(blank=True, null=True)
    last_modified_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_modified_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,)

    def __str__(self) -> str:
        return self.name.capitalize()

class QuestionCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
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
    answer_prefix = models.TextField(null=True, blank=True)
    correct_answer = models.CharField(max_length=255, null=True, blank=True)
    marks = models.FloatField(default=1.0)
    last_modified_at = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,)

    def __str__(self):
        return f"{self.pk} - {self.name}"
    
    @property
    def next(self) -> Optional["Question"]:
        return Question.objects.filter(pk__gt=self.pk, category=self.category).order_by('id').first()
    
    @property
    def previous(self) -> Optional["Question"]:
        return Question.objects.filter(pk__lt=self.pk, category=self.category).order_by('id').last()
    
    @property
    def _uuid(self) -> str:
        return str(self.uuid)
    
class Batch(models.Model):
    name = models.CharField(max_length=255)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    categories = models.ManyToManyField(QuestionCategory)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    @property
    def students_count(self) -> int:
        return self.student_set.count()
    
    def adjust_state(self):
        if self.end_date < datetime.now():
            self.is_active = True

class StudentAnswer(models.Model):
    student = models.ForeignKey("authentication.Student", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.TextField()
    answer = models.CharField(max_length=255)
    score = models.FloatField(default=0.0)
    is_correct = models.BooleanField(default=False)
    last_modified_at = models.DateTimeField(auto_now_add=True)