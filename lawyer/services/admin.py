from django.contrib import admin
from .models import Post, Client, Review, Service, Comment, Group
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'pub_date')
    list_display_links = ('title', )
    search_fields = ('title', 'text', 'pub_date')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'phone')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date')
    list_display_links = ('text',)
    
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'pers', 'group', 'price')
    list_display_links = ('title',)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'post', 'author')
    list_display_links = ('text',)
    search_fields = ('post', 'author')


admin.site.register(Post, PostAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)

