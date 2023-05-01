from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_id = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=15)
    dob = models.DateField(null=True, blank=True)
    timezone = models.CharField(max_length=50, default="Asia/Kolkata")
    profile_picture = models.CharField(max_length=256, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_modified_at = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="last_updated_by")