from django.contrib import admin
from .models import Post, Client, Review, Service, Comment, Group, Banner
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'pub_date', 'image')
    list_display_links = ('title', )
    search_fields = ('title', 'text', 'pub_date')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'full_name', 'phone', 'email', 'service')
    list_display_links = ('full_name', )
    search_fields = ('full_name', 'phone')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date')
    list_display_links = ('text',)
    
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'pers', 'group', 'description', 'price')
    list_display_links = ('title',)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'post', 'author')
    list_display_links = ('text',)
    search_fields = ('post', 'author')

class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    list_display_links = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Banner, BannerAdmin)
