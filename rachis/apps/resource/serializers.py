from django.contrib.postgres.fields import ArrayField
from rest_framework import serializers
from .models import Resource

class ResourceSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=10) 
    tags = ArrayField(
        serializers.CharField(max_length=300),
        blank=True, default=list)
    snippet_one = serializers.ImageField(required=False)
    snippet_two = serializers.ImageField(required=False)
    snippet_three = serializers.ImageField(required=False)
    video_file = serializers.FileField(required=False)
    link = serializers.URLField(max_length=200)

    class Meta:
        model = Resource
        fields = ['title', 'description', 'author', 'tags', 'snippet_one',
        'snippet_two', 'snippet_three', 'video_file', 'link']    
