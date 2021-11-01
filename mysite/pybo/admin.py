from django.contrib import admin
from .models import Question #.models에서 Question 가져와서

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin) #admin에 등록록# Register your models here.
