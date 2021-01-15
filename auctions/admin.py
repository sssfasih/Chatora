from django.contrib import admin

from .models import AuctionProduct,ProductCategory,Bid,Comment
# Register your models here.

admin.site.register(AuctionProduct)
admin.site.register(ProductCategory)
admin.site.register(Bid)
admin.site.register(Comment)

