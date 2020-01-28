from django.contrib import admin
from .models import Author, Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)
