from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(QuestionCategory)
admin.site.register(Question)
admin.site.register(Batch)
admin.site.register(Language)