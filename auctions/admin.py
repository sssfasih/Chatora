from django.contrib import admin

from .models import AuctionProduct,ProductCategory,Bid,Comment

class AuctionWatchers(admin.ModelAdmin):
    filter_horizontal = ('watchers',)

# Register your models here.

admin.site.register(AuctionProduct,AuctionWatchers)
admin.site.register(ProductCategory)
admin.site.register(Bid)
admin.site.register(Comment)

