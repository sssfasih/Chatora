from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_pic = models.ImageField(default="")

    def __str__(self):
        return str(self.username)

class Follow(models.Model):
    user = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    following = models.ForeignKey(User,related_name="follower",blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return "Follow object by "+str(self.user.username)

class Post(models.Model):
    posted_by = models.ForeignKey(User, related_name="posted_by", on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    likes = models.ManyToManyField(User,related_name='liked',blank=True)

    def __str__(self):
        return "Post object by " + str(self.by.username)
