from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass


class Message(models.Model):
    Text = models.CharField(max_length=200)
    From = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    Read_by = models.ManyToManyField(User,related_name='read')
    #To = models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')

    def __str__(self):
        return f"Msg From {self.From}"

class Conversation(models.Model):
    participants = models.ManyToManyField(User,related_name='participant')
    Messages = models.ManyToManyField(Message,related_name='texts')
    Last_Updated = models.DateTimeField(auto_now=True)