from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post, Tag, Author
from posts.serializers import AuthorSerializer, TagSerializer, PostSerializer
from rest_framework import status 

# class PostView(APIView):
    
    
#     def get(self, resquest):
        
#         posts_title = [post.title for post in Post.objects.all()]
#         posts_content = [post.content for post in Post.objects.all()]
        
#         return Response({"title":posts_title, "content":posts_content})


class PostView(APIView):
    
    def get(self, request):
        
        posts = Post.objects.all()
        
        serializer = PostSerializer(posts, many=True)
        
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



class TagView(APIView):
    
    def get(self, request):
        
        tags = Tag.objects.all()
        
        serializer = TagSerializer(tags, many=True)
        
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class AuthorView(APIView):
    
    def get(self, request):
        
        authors = Author.objects.all()
        
        serializer = AuthorSerializer(authors, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)