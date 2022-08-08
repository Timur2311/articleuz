from django.contrib import admin

# Register your models here.
from .models import Article, Comment, SavedArticles, Tags

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(SavedArticles)
admin.site.register(Tags)