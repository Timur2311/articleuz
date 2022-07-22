# from django.shortcuts import render

from post.serializer import MainPostsSerializer, CommentSerializer
from rest_framework import generics
from post.models import Article
from common.models import User

class MainPostsListView(generics.ListAPIView):
    serializer_class = MainPostsSerializer
    
    def get_queryset(self):
        return Article.objects.all()[:4]
    
class ReadNextListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = MainPostsSerializer
    
class AddCommentView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = CommentSerializer
    
    
    
class PopularPostListView(generics.ListAPIView):
    
    serializer_class = MainPostsSerializer
    
    def get_queryset(self):
        return Article.objects.filter(is_popular = True)

class ForYouListView(generics.ListAPIView):
    serializer_class = MainPostsSerializer
    
    def get_queryset(self, request):
        selected_tags = User.objects.get(id = request.user.id).selected_tags
        results = []
        for tag in selected_tags:
            for article in tag.tag_articles:
                results.append(article)
        return  results

class ArticleDetailView(generics.RetrieveAPIView):
    serializer_class = MainPostsSerializer
    lookup_field="id"
    
    
    
    
