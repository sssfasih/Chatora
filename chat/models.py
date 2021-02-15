from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass


class Message(models.Model):
    Text = models.CharField(max_length=200)
    From = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    To = models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
