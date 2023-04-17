from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

TYPE_CHOICES = (
    ('trivia','TRIVIA'),
    ('riddle', 'RIDDLE'),
    ('none', 'NONE'),
    ('bunq history', 'BUNQ HISTORY'),
)


# Create your models here.
class Question(models.Model):
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    riddle = models.CharField(unique=False, blank=True, max_length=250)
    answer = models.CharField(unique=False, blank=True, max_length=250)
    secondary_answer = models.CharField(unique=False, blank=True, max_length=250, default='something random with oqeiwuweywe')
    question_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='none')


    def __str__(self):
        return self.riddle
    
class Answer(models.Model):
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name = 'related_question')
    answer = models.TextField(unique=False, blank=True)
    correct = models.BooleanField()
    adam = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    

    def __str__(self):
        return self.question.riddle +" Correct: "+ str(self.correct) +" - "+ self.adam.username
    