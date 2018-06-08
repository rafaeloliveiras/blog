from django.contrib import admin
from .models import Post, Category
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)


class ArticleAdmin(admin.ModelAdmin):
    class Media:
        js = ('/path/tiny_mce/tiny_mce.js')