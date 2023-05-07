from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(QuestionCategory)
admin.site.register(Batch)
admin.site.register(StudentAnswer)
admin.site.register(Question)

# class QuestionModelOptions(admin.TabularInline):
#     fields = (... , "index",)
#     # define the sortable
#     sortable_field_name = "index"

# admin.site.register(Question, QuestionModelOptions)