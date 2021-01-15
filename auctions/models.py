from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class ProductCategory(models.Model):
    category = models.CharField(max_length=60)

class AuctionProduct(models.Model):
    name = models.CharField(max_length=60)
    cat_id = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name='cat_id')
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='started_by')
    highest = models.IntegerField()
    winner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='winner')


class Bid(models.Model):
    bidder = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bidder')
    prod_id = models.ForeignKey(AuctionProduct,on_delete=models.CASCADE,related_name='bidProduct')

class Comment(models.Model):
    commenter = models.ForeignKey(User,on_delete=models.CASCADE,related_name='commenter')
    text = models.CharField(max_length=600)
    prod_id = models.ForeignKey(AuctionProduct,on_delete=models.CASCADE,related_name='comProduct')

