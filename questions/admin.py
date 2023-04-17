from django.contrib import admin
from .models import Question, Answer



class Questiondmin(admin.ModelAdmin):
    list_display = ('riddle', 'question_type', 'get_url')
    list_filter = ('question_type', 'date_created', 'date_modified')
    search_fields = ['riddle']

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'correct', 'adam','question')
    list_filter = ('correct', 'adam', 'date_created', 'date_modified')
    search_fields = ['comment_text']

# Register your models here.
admin.site.register(Question, Questiondmin)
admin.site.register(Answer, AnswerAdmin)
