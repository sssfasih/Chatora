from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class ProductCategory(models.Model):
    category = models.CharField(max_length=60)


    def __str__(self):
        return f"{self.category}"

class AuctionProduct(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(default="")
    desc = models.CharField(max_length=600,default="")
    cat_id = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name='cat_id')
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='started_by')
    highest = models.IntegerField(default=0)
    winner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='winner',blank=True,null=True)

    def __str__(self):
        return f"{self.name} by {self.owner}"

class Bid(models.Model):
    bidder = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bidder')
    prod_id = models.ForeignKey(AuctionProduct,on_delete=models.CASCADE,related_name='bidProduct')

    def __str__(self):
        return f"Bid by {self.bidder}"

class Comment(models.Model):
    commenter = models.ForeignKey(User,on_delete=models.CASCADE,related_name='commenter')
    text = models.CharField(max_length=600)
    prod_id = models.ForeignKey(AuctionProduct,on_delete=models.CASCADE,related_name='comProduct')


    def __str__(self):
        return f"Comment by {self.commenter} on {self.prod_id}"
