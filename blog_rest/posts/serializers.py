# from rest_framework.serializers import Serializer 
from rest_framework import serializers 
from posts.models import Tag, Author, Post
from django.shortcuts import get_object_or_404


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        return Tag.objects.create(**validated_data)
        # return Tag.objects.create(name=validated_data.get('name')) tek parametre olsaydı bu şekilde de datayı ekleyebilirdik.
    

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField()
    
    def create(self, validated_data):
        return Author.objects.create(**validated_data)
    

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    content = serializers.CharField() 
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField()
    
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(many=True, required=False, read_only=True)
    
    author_id = serializers.IntegerField(write_only=True)
    tag_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )
    
    
    def create(self, validated_data):
        author_id = validated_data.pop('author_id')
        tag_ids = validated_data.pop('tag_ids', []) #key'i bulamazsa none yerine boş liste dönsün.
        
        author = get_object_or_404(Author, id=author_id)
        post = Post.objects.create(author=author, **validated_data)
        
        if tag_ids:
            tags = Tag.objects.filter(id__in=tag_ids)
            post.tags.set(tags)
        
        return post