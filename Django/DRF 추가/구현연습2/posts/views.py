from django.shortcuts import get_object_or_404

from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(post_id = self.kwargs['post_id'])


class LikeView(views.APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        is_created = post.likes.get_or_create(author=request.user)
        
        if not is_created:
            return Response(status=status.HTTP_409_CONFLICT)
        
        return Response(status=status.HTTP_201_CREATED)
    
    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like = get_object_or_404(Like, author = request.user)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) #삭제 시 204응답