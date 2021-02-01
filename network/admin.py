from django.contrib import admin

from .models import Post,User,Follow
# Register your models here.
'''
class FollowAdmin(admin.ModelAdmin):
    filter_horizontal = ('following',)
'''
class AnotherAdmin(admin.ModelAdmin):
    filter_horizontal = ('likes',)


admin.site.register(Post,AnotherAdmin)
admin.site.register(User)
admin.site.register(Follow,) #FollowAdmin)

