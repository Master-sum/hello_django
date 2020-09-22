from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'article', 'creat_time','root','parent','reply_to']
    fields = ['name',  'text', 'article','creat_time','root','parent','reply_to']


admin.site.register(Comment, CommentAdmin)
