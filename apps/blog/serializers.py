from rest_framework import serializers
from .models import *

class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
       model = Images
       fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    images = BlogImageSerializer(many=True, allow_null=True)
    user = serializers.CharField(read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Blogs
        fields = ['id', 'main_image', 'title', 'text', 'slug', 'date', 'category', 'count', 'images', 'user', 'likes_count']

    def get_likes_count(self, instance):
        return instance.liked_post.all().count()


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Like
        fields = '__all__'