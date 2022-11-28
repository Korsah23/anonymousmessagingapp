from django.db import models
from datetime import datetime

# Create your models here.

class Message(models.Model):
    userId = models.CharField(max_length=8)
    userMessage = models.CharField(max_length=10000)
    timePosted = models.DateTimeField(default=datetime.now, blank=True)


    
