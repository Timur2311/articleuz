# from django.shortcuts import render

from post.serializer import MainPostsSerializer, CommentSerializer
from rest_framework import generics
from post.models import Article, Tags

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from post.models import Article
from post.serializer import MainPostsSerializer
from rest_framework import mixins
from rest_framework import generics


class PostUpdate(generics.GenericAPIView, 
               mixins.UpdateModelMixin):
    queryset = Article.objects.all()
    serializer_class = MainPostsSerializer
    lookup_field = "id"
    
    def get_queryset(self):
        
        return Article.objects.get(id=id)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    

    def perform_update(self, serializer):
    # Save with the new value for the target model fields
        post = self.get_object()
        post.update_count+=1        
        serializer.save()


class ListCreatePostApiView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = MainPostsSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MainPostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostCreateListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = MainPostsSerializer


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
        return Article.objects.filter(is_popular=True)


class ForYouListView(generics.ListAPIView):
    serializer_class = MainPostsSerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        tag_ids = Tags.objects.all().filter(user_selected_tags=self.request.user)
        return queryset.filter(tags=tag_ids)


class ArticleDetailView(generics.RetrieveAPIView):
    serializer_class = MainPostsSerializer
    lookup_field = "id"
