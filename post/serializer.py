from rest_framework import serializers
from post.models import Article, Comment



class MainPostsSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = '__all__'
        
class CommentSerializer(serializers.Serializer):
    article = MainPostsSerializer()
    class Meta:
        model = Comment
        fields = "__all__"
        
