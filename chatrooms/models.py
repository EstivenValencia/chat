from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

class ChatMessage(models.Model):
	content = models.CharField(db_column="content", max_length=1000)
	timestamp = models.DateTimeField(db_column="date", auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
