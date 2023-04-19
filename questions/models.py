from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from core.settings import HOST_URL
from django.core.signing import Signer
import uuid

signer = Signer()


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
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.riddle
    
    def get_url(self):
        secret = signer.sign(str(self.id))
        return HOST_URL+"/qr/"+secret



class Answer(models.Model):
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, related_name='testtest')
    answer = models.TextField(unique=False, blank=True)
    correct = models.BooleanField()
    adam = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.riddle
    
    
