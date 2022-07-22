
from django.db import models
from common.models import Author, User
class Tags(models.Model):
    title = models.CharField(max_length=16)
    slug = models.SlugField()
    
    
class Article(models.Model):
    
    title = models.CharField(max_length=4096)
    image = models.ImageField(upload_to="artciles/")
    description = models.TextField(max_length=4096)
    content = models.TextField()
    
    tags = models.ManyToManyField(Tags, related_name="tag_articles")
    
    author = models.ForeignKey('common.Author', verbose_name="articles", on_delete=models.CASCADE)
    
    view_count = models.PositiveBigIntegerField(default=0)
    is_popular = models.BooleanField(default=False)
    read_time = models.PositiveIntegerField(default=1)
    
    created_at = models.DateField(auto_now_add=True)
    
    
    
class Comment(models.Model):
    user = models.ForeignKey("common.User", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    
class SavedArticles(models.Model):
    user = models.ForeignKey("common.User", on_delete=models.CASCADE)
    articles = models.ManyToManyField(Article, related_name="saved_articles")
    
    
