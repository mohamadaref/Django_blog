from django.contrib import admin
from blog.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title' , 'slug' , 'author' , 'publish' , 'updated' , 'status')
    list_filter = ('author' , 'publish' , 'updated' , 'status')
    search_fields = ('title' , 'body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name' , 'post' , 'body' , 'email' , 'created' , 'active')
    list_filter = ('active' , 'name' , 'post' , 'email')
    search_fields = ('body' ,)
    date_hierarchy = 'created'
    ordering = ['active', 'created']

admin.site.register(Post , PostAdmin)
admin.site.register(Comment , CommentAdmin)
# Register your models here.
