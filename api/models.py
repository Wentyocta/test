from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class Message(models.Model):
	text = models.TextField()
	success = models.BooleanField(default=True)
	created_date = models.DateTimeField(auto_now_add=True)