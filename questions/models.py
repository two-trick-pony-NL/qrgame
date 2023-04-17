from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    riddle = models.CharField(unique=False, blank=True, max_length=250)
    answer = models.CharField(unique=False, blank=True, max_length=250)
    secondary_answer = models.CharField(unique=False, blank=True, max_length=250)
    question = models.CharField(unique=False, blank=True, max_length=250)

    def __str__(self):
        return self.riddle
    
class Answer(models.Model):
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, null=True, related_name = 'related_question')
    answer = models.TextField(unique=False, blank=True)
    correct = models.BooleanField()
    adam = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    

    def __str__(self):
        return self.question.riddle +" Correct: "+ str(self.correct) +" - "+ self.adam.username
    