from django.contrib import admin
from .models import Leaderboard

# Register your models here.



class ObjectAdmin(admin.ModelAdmin):
    ordering = ['-score']
    list_filter = ('adam', 'score')

    

admin.site.register(Leaderboard, ObjectAdmin)

