from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Leaderboard(models.Model):
    adam = adam = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,)
    score = models.IntegerField()

    def __str__(self):
        return str(self.score) +"  "+ self.adam.username 