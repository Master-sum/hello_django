from django.contrib import admin
from .models import Category,Tag,Article
class AcrticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'creat_time', 'late_time', 'category', 'author']
    fields = ['title', 'content', 'excerpt', 'category', 'tags']
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(AcrticleAdmin, self).save_model(request,obj,form,change)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)